(n, a) = map(int, input().split())
c = 0
d = 1000
for i in range(1, n + 1):
    c += a + i - 1
    d = min(abs(a + i - 1), d)
if a < 0 and a - n <= 0:
    print(c + d)
else:
    print(c - d)
