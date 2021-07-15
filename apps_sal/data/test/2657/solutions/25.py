n = int(input())
a = list(map(int, input().split()))
a.sort()
m = a[-1]
mid = m / 2

d = 10 ** 9
for ai in a[:-1]:
    x = abs(mid - ai)
    if x < d:
        ans = ai
        d = x

print(m, ans)
