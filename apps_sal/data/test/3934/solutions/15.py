import sys
N = int(input())
Edge = [[] for _ in range(N)]
Dim = [0] * N
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
    Dim[a] += 1
    Dim[b] += 1
Leaf = [d for d in Dim if d == 1]
if [d for d in Dim if d == 2]:
    print('NO')
elif len(Leaf) * (len(Leaf) - 1) // 2 < N - 1:
    print('NO')
else:
    print('YES')
