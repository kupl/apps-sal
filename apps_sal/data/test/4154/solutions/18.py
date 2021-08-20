(N, M) = map(int, input().split())
L = [0 for _ in range(N)]
for i in range(M):
    (l, r) = map(int, input().split())
    l -= 1
    r -= 1
    L[l] += 1
    if r + 1 < N:
        L[r + 1] -= 1
S = [0]
for i in range(N):
    temp = L[i] + S[-1]
    S.append(temp)
ans = 0
for i in range(1, N + 1):
    if S[i] == M:
        ans += 1
print(ans)
