for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a <= b:
        print(b)
        continue
    if c <= d:
        print(-1)
        continue
    m = a - b
    t = 0 - -m // (c - d)
    print(b + t * c)
