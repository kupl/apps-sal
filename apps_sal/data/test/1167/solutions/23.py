t = int(input())
for i in range(t):
    a, b, c, d, k = [int(i) for i in input().split()]
    if a % c == 0:
        x = a // c
    else:
        x = a // c + 1
    if b % d == 0:
        y = b // d
    else:
        y = b // d + 1
    if x + y <= k:
        print(x, y)
    else:
        print(-1)
