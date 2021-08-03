n, t = map(int, input().split())
tl = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if tl[i] >= t and tl[i] - tl[i - 1] >= t:
        ans += t
    else:
        ans += tl[i] - tl[i - 1]
print(ans + t)
