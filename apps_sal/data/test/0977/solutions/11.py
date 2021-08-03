def solve(n, p, x, a):
    res_ptn = 1
    r = 0
    for l in range(n):
        while r < n and a[r] <= x + l:
            r += 1
        res_ptn *= r - l
        res_ptn %= p
    return res_ptn != 0


n, p = map(int, input().split())
a = list(map(int, input().split()))


a = sorted(a)
ans = []
for x in range(1, 2000 + 2):
    if solve(n, p, x, a):
        ans.append(x)

print(len(ans))
print(*ans)
