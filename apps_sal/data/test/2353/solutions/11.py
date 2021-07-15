t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split()))
    if b >= a:
        print(b)
    elif d >= c:
        print(-1)
    else:
        k = (a - b + c - d - 1) // (c - d)
        print(b + k * c)


