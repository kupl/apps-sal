a, b, x = map(int, input().split())
A = a + ((x - (a % x)) % x)
B = b - (b % x)
print((B - A) // x + 1 if B >= A else 0)
