A, B, X = map(int, input().split())


def d(n):
    return len(str(n))


N = 10 ** 9 + 1
up = N
down = 0
while True:
    mid = (down + up) // 2
    if mid == down:
        break
    if X < A * mid + B * d(mid):
        up = mid
    else:
        down = mid
print(down)
