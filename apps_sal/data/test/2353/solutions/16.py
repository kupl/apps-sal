t = int(input())
for ii in range(t):
    (a, b, c, d) = map(int, input().split())
    if b >= a:
        print(b)
    elif c - d <= 0:
        print(-1)
    else:
        print(b + c * ((a - b + c - d - 1) // (c - d)))
