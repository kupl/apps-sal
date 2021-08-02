N, M = map(int, input().split())
A = list(map(int, input().split()))
D = [(A[i], 1) for i in range(N)]

for i in range(M):
    B, C = (map(int, input().split()))
    D.append((C, B))

D.sort()
D.reverse()

ans, left = 0, N
for (i, j) in D:
    use = min(j, left)
    ans += use * i
    left -= use
print(ans)
