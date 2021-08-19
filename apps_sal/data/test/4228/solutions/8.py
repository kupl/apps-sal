(N, L) = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    if L - 1 >= 0 and i == 1:
        continue
    if L - 1 < 0 and L + N - 1 >= 0 and (i == 1 - L):
        continue
    if L - 1 < 0 and L + N - 1 < 0 and (i == N):
        continue
    ans += L + i - 1
print(ans)
