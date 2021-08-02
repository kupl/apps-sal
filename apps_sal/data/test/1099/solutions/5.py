import sys
input = sys.stdin.readline
n = int(input())

E = [[] for i in range(n + 1)]
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    E[x].append(y)
    E[y].append(x)

C = [-1] * (n + 1)
Q = [1]
C[1] = 0
while Q:
    x = Q.pop()

    for to in E[x]:
        if C[to] == -1:
            C[to] = 1 - C[x]
            Q.append(to)

B = C.count(0)
W = C.count(1)

print(min(B, W) - 1)
