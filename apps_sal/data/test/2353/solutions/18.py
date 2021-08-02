t = int(input())
for i in range(t):
    a, b, c, d = list(map(int, input().split()))
    if b >= a:
        print(b)
        continue
    if c <= d:
        print(-1)
        continue
    x = c - d
    y = (a - b + c - d - 1) // x
    print(b + y * c)
