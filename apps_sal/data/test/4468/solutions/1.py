n, t = map(int, input().split())
T = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    if T[i] - T[i - 1] >= t:
        ans += t
    else:
        ans += T[i] - T[i - 1]
print(ans + t)
