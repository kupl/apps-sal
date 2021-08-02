N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
for n in range(1, N):
    timeD = t[n] - t[n - 1]
    if T >= timeD:
        ans += timeD
    else:
        ans += T
ans += T
print(ans)
