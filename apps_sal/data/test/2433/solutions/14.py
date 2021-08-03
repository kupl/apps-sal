t = int(input())
for i in range(t):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    if h < c:
        h, c = c, h
        p, f = f, p

    b //= 2

    resp = 0
    ff = min(b, p)
    b -= ff
    resp += h * ff

    ff = min(b, f)
    resp += c * ff
    print(resp)
