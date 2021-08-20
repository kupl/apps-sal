t = int(input())
for i in range(t):
    (x, y, p, q) = map(int, input().split())
    if p == q:
        if x != y:
            print(-1)
        elif x == y == 0:
            print(1)
        else:
            print(0)
        continue
    if p == 0:
        if x == 0:
            if y == 0:
                print(1)
            else:
                print(0)
        else:
            print(-1)
        continue
    k = max((y - x + q - p - 1) // (q - p), (x + p - 1) // p)
    print(k * q - y)
