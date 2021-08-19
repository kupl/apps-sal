def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
(H, W) = list(map(int, input().split()))
(h, w) = list(map(int, input().split()))
print((H - h) * (W - w))
