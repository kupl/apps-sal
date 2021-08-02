class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, new):
        self.items.append(new)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


L = [int(s) for s in input().split()]
n, m = L[0], L[1]
S = [[] for i in range(n)]
for i in range(m):
    Side = [int(s) for s in input().split()]
    S[Side[0] - 1].append(Side[1] - 1)
    S[Side[1] - 1].append(Side[0] - 1)

result = 0
visited = [False for i in range(n)]
color = [None for i in range(n)]
q = Stack()
for i in range(n):
    if S[i] != [] and not visited[i]:
        q.push(i)
        color[i] = "a"
        visited[i] = True
        cycle = False
        while not q.empty():
            j = q.pop()
            color[j] = "b"
            for k in S[j]:
                if visited[k] and color[k] == "a":
                    cycle = True
                if not visited[k]:
                    q.push(k)
                    visited[k] = True
                    color[k] = "a"

        if not cycle:
            result += 1
    if S[i] == []:
        result += 1
print(result)
