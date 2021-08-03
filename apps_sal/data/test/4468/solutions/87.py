N, T = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 0

for i in range(N - 1):
    tmp = t[i + 1] - t[i]
    ans += min(tmp, T)

print(ans + T)
