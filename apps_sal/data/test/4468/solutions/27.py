n, t = list(map(int, input().split()))
tl = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    ans += min(tl[i] - tl[i - 1], t)
ans += t
print(ans)
