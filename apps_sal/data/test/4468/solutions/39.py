N, T = map(int, input().split())
time = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    if time[i + 1] - time[i] >= T:
        ans += T
    else:
        ans += time[i + 1] - time[i]
print(ans + T)
