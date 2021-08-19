def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:  # a<=b
            c = a
            a = b
            b = c
        b %= a
    return max(a, b)


n, x = map(int, input().split())
d = sorted(list(map(lambda a: abs(a - x), list(map(int, input().split())))))
now = d[0]
for i in d[1:]:
    now = gcd(now, i)
print(now)
