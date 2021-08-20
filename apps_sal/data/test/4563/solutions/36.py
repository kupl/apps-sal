def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):
    return x * y // gcd(x, y)


N = int(input())
(x, y) = (0, 0)
for i in range(N):
    p = 0
    (T, A) = map(int, input().split())
    if i == 0:
        (x, y) = (T, A)
        continue
    if x <= T and y <= A:
        (x, y) = (T, A)
    elif x <= T and A < y:
        if y % A != 0:
            p = 1
        x = T * (y // A + p)
        y = A * (y // A + p)
    elif T < x and y <= T:
        if x % T != 0:
            p = 1
        y = A * (x // T + p)
        x = T * (x // T + p)
    elif x // T + 1 <= y // A + 1:
        if y % A != 0:
            p = 1
        x = T * (y // A + p)
        y = A * (y // A + p)
    else:
        if x % T != 0:
            p = 1
        y = A * (x // T + p)
        x = T * (x // T + p)
print(x + y)
