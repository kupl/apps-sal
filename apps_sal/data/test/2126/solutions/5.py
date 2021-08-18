n, m, h = [int(i) for i in input().split()]
front = [int(i) for i in input().split()]
left = [int(i) for i in input().split()]
A = []
for i in range(n):
    B = [int(i) for i in input().split()]
    A.append(B)

ans = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if A[i][j]:
            ans[i][j] = min(front[j], left[i])
for i in ans:
    print(*i)
