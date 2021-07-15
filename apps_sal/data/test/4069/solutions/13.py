x, k, d = map(int, input().split())
x = abs(x)
l = x // d

if k <= l:
    print(abs(x - k * d))
else:
    print(abs(abs(x - d * l) - d * ((k - l) % 2)))
