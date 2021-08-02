import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

c1 = list(map(int, input()[:-1].split()))
c2 = list(map(int, input()[:-1].split()))
c3 = list(map(int, input()[:-1].split()))

al = [list() for _ in range(n)]

for _ in range(n - 1):
    u, v = list(map(int, input()[:-1].split()))
    al[u - 1].append(v - 1)
    al[v - 1].append(u - 1)

for i in range(n):
    if len(al[i]) > 2:
        print(-1)
        return
    elif len(al[i]) == 1:
        start = i

vis = [False for _ in range(n)]
sequence = []
stack = deque()
stack.append(start)

while len(stack) > 0:
    u = stack.pop()
    sequence.append(u)
    vis[u] = True
    for v in al[u]:
        if not vis[v]:
            stack.append(v)

sums = [0] * 6
seqs = [[c1, c2, c3], [c1, c3, c2], [c2, c1, c3], [c2, c3, c1], [c3, c1, c2], [c3, c2, c1]]
seqi = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

for i in range(n):
    for j in range(6):
        sums[j] += seqs[j][i % 3][sequence[i]]

mini = 0
mn = sums[0]

for i in range(len(sums)):
    if sums[i] < mn:
        mn = sums[i]
        mini = i
ans = [0] * n
for i in range(n):
    ans[sequence[i]] = seqi[mini][i % 3]
print(mn)
print(*ans)
