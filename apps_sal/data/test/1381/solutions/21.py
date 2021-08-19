(k, n, s, p) = (int(i) for i in input().split())
L = k * (n // s + int(bool(n % s)))
print(L // p + int(bool(L % p)))
