(a, b) = list(map(int, input().split()))
(z, x, y) = list(map(int, input().split()))
A = z * 2 + x
B = 3 * y + x
print(max(0, A - a) + max(0, B - b))
