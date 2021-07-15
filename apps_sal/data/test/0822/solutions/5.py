n, m, z = map(int, input().split())

gcd = lambda a, b: gcd(b, a % b) if b else a
mm = n * m // gcd(n, m)
print(z // mm)
