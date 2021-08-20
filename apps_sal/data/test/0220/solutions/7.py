(s, x) = map(int, input().split())
print(0 if s < x or s - x & 2 * x + 1 else 2 ** bin(x).count('1') - 2 * (s == x))
