[n, x], cur, ans = list(map(int, input().split())), 1, 0
for i in range(n):
    l, r = list(map(int, input().split()))
    cur += (l - cur) // x * x
    ans += r - cur + 1
    cur = r + 1
print(ans)
