a, b, c = list(map(int, input().split()))

m = max(a, b, c)
sub = 3 * m - a - b - c

if sub % 2 != 0:
    sub += 3

print((sub // 2))

