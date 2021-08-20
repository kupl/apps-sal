(a, b) = map(int, input().split(' '))
(c, d) = map(int, input().split(' '))
j = 0
if c == a or b == d:
    j = 2
print((abs(c - a) + 1) * 2 + 2 * (abs(b - d) + 1) + j)
