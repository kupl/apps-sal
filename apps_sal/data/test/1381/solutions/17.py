k, n, s, p = [int(x) for x in input().split()]

lists = n // s + (0 if n % s == 0 else 1)

needed = k * lists

print(needed // p + (0 if needed % p == 0 else 1))
