n = int(input())
a, b, c = 0, 0, 0
for i in range(n):
    x, y = map(int, input().split())
    a += x
    b += y
    if not c and (x + y) % 2: c = 1
a, b = a % 2, b % 2
print(a if a == b and (a == 0 or a == c) else -1)
