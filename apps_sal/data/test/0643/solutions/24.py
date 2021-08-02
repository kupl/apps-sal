def div(a, b):
    return (a + b - 1) // b


for t in range(int(input())):
    x, y, p, q = map(int, input().split())
    if q == 1:
        if p == 0 and x == 0 or p == 1 and x == y:
            print(0)
        else:
            print(-1)
    else:
        z = max(max(div(x, p), div(y, q)), max(div(y - x, q - p), 0))
        print(z * q - y)
