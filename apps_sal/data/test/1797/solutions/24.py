class node:
    def __init__(self, index):
        self.index = index
        self.nextN = None
        self.visited = 0


n = int(input())
nodes = [node(i + 1) for i in range(n)]
c = [int(i) for i in input().split()]
i = 0
while i < n:
    nodes[i].nextN = nodes[c[i] - 1]
    i += 1

sequence = []

i = 0
news = []
while i < n:
    x = i
    while(nodes[x].visited != 1):
        news.append(nodes[x])
        nodes[x].visited = 1
        x = nodes[x].nextN.index - 1
    sequence.append(news)
    news = []
    i += 1
sequence.sort(key=len, reverse=True)
if(n == 1):
    print(1)
elif(n == 2):
    print(4)
else:
    x = len(sequence[0]) + len(sequence[1])
    x *= x
    som = 0
    for i in range(2, n):
        value = len(sequence[i])
        if(value == 0):
            break
        som += value * value
    print(x + som)
