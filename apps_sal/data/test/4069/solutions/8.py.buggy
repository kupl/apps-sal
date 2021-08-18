x, k, d = map(int, input().split())

x = abs(x)

if x - k * d >= 0:
    print(x - k * d)
    return

k -= x // d
if k % 2:
    print(d - x % d)
else:
    print(x % d)
