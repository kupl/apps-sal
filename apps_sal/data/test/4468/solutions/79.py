(n, t) = map(int, input().split())
tl = list(map(int, input().split()))
ans = t
for i in range(n - 1):
    if tl[i + 1] - tl[i] >= t:
        ans += t
    else:
        ans += t - (t - (tl[i + 1] - tl[i]))
print(ans)
