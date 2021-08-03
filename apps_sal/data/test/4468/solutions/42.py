N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    d = t[i] - t[i - 1]
    if d < T:
        ans += d
    else:
        ans += T
print(ans + T)
