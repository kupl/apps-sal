(N, M) = map(int, input().split())
H = list(map(int, input().split()))
A = [True for i in range(N)]
for i in range(M):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    if H[a] <= H[b]:
        A[a] = False
    if H[b] <= H[a]:
        A[b] = False
ans = 0
for i in range(N):
    if A[i]:
        ans += 1
print(ans)
