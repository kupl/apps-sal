N, A, B = map(int, input().split())
diff = A - B
H = [int(input()) for i in range(N)]


def check(x):
    time = 0
    _H = [h - B * x for h in H]
    for _h in _H:
        if _h > 0:
            time += -(-_h // diff)
    return time <= x


left = 0  # False
right = 10**10  # True
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
