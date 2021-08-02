n = int(input())
a, b, c, d = 2 * 10**9, 0, 10**9, -10**9

for i in range(n):
    x, y = list(map(int, input().split()))
    a = a if a < x + y else x + y
    b = b if b > x + y else x + y
    c = c if c < y - x else y - x
    d = d if d > y - x else y - x

print((b - a if b - a > d - c else d - c))
