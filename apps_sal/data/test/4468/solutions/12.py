N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    ans += min(t[i] - t[i - 1], T)
print(ans + T)
