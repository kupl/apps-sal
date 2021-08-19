(l, r) = map(int, input().split())
mod = 2019
a = l % mod
b = r % mod
if r - l >= 2018:
    print(0)
elif a > b:
    print(0)
else:
    t = a * (a + 1) % mod
    for x in range(a, b):
        for y in range(x + 1, b + 1):
            if x * y % mod < t:
                t = x * y % mod
    print(t)
