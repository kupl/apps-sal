(a, b) = list(map(int, input().split()))
(x, y, z) = list(map(int, input().split()))
c = 2 * x + y
d = y + 3 * z
print(max(c - a, 0) + max(d - b, 0))
