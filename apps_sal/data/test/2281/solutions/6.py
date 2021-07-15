n = int(input())
r = list(range(n))
a, b = r[2 - n % 2::2], r[1 + n % 2::2]
print(' '.join(map(str, a + [n] + a[::-1] + b + b[::-1] + [n])))
