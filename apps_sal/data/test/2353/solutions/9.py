t = int(input())
while t > 0:
    t -= 1
    a, b, c, d = map(int, input().split())
    if b < a and c <= d:
        print('-1')
    elif b >= a:
        print(b)
    else:
        print(b + (a - b + c - d - 1) // (c - d) * c)
