n = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7


def lcm(X, Y):
    x = X
    y = Y
    if y > x:
        (x, y) = (y, x)
    while x % y != 0:
        (x, y) = (y, x % y)
    return X * Y // y


cnt = 0
ans = 0
LCM = 1
for i in range(n):
    Q = lcm(LCM, A[i])
    cnt *= Q // LCM
    LCM = Q
    cnt += Q // A[i]
print(cnt % mod)
