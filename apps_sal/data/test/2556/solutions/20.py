n = int(input())
for i in range(n):
    a, b = [int(x) for x in input().split(' ')]
    if a >= b:
        print(b)
    else:
        c = int(b / a)
        d = b % a
        print((a - d) * c**2 + d * (c + 1)**2)
