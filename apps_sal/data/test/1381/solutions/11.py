(k, n, s, p) = map(int, input().split())
t = n // s + bool(n % s)
print(k * t // p + bool(k * t % p))
