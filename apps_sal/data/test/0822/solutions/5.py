n, m, z = map(int, input().split())


def gcd(a, b): return gcd(b, a % b) if b else a


mm = n * m // gcd(n, m)
print(z // mm)
