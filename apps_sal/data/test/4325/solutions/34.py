n, xi, t = (int(x) for x in input().split())
c = n // xi
a = n % xi
if a == 0:
    print(c * t)
else:
    print((c + 1) * t)
