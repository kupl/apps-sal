n = int(input())

ra, rb = 1, 1
for i in range(n):
    a, b = map(int, input().split())
    n = max((ra + a - 1) // a, (rb + b - 1) // b)
    ra = a * n
    rb = b * n

print(ra + rb)
