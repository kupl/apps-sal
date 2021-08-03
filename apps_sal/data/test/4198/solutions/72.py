A, B, X = map(int, input().split(' '))


def cost(N):
    return A * N + B * len(str(N))


if cost(0) > X:
    print(0)
    return
if cost(10 ** 9) <= X:
    print(10 ** 9)
    return

top = 10 ** 9
bottom = 1
while top - bottom > 1:
    mid = (top + bottom) // 2
    if cost(mid) <= X:
        bottom = mid
    else:
        top = mid
print(bottom)
