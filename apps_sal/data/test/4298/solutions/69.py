n, d = map(int, input().split())
d = d * 2 + 1
if n % d == 0:
    print(n // d)
else:
    print(n // d + 1)
