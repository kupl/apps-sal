(a, b) = map(int, input().split())
(c, d) = (0, 0)
if a % 2 == 1:
    c = a
    a += 1
if b % 2 == 0:
    d = b
    b -= 1
print((b - a + 1) // 2 % 2 ^ c ^ d)
