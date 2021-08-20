from _collections import defaultdict
n = int(input())
f = 0
s = 0
gen = defaultdict(list)
for i in range(n - 1):
    (a, b) = map(lambda x: int(x), input().split())
    gen[a].append(b)
    gen[b].append(a)
start = [1]
visited = set()
Turn = True
while start:
    q = []
    for i in start:
        visited.add(i)
        for j in gen[i]:
            if j not in visited:
                q.append(j)
    if Turn:
        f += len(start)
    else:
        s += len(start)
    Turn = not Turn
    start = q
print(f * s - (n - 1))
