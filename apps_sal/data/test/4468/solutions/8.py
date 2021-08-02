N, T = map(int, input().split())
L = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    ans += min(L[i + 1] - L[i], T)
print(ans + T)
