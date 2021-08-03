n, m = map(int, input().split())

if m >= 2 and n >= 2:
    ans = (n - 2) * (m - 2)
elif m == 1 and n == 1:
    ans = 1
elif m == 1 or n == 1:
    ans = n * m - 2
else:
    ans = 0

print(ans)
