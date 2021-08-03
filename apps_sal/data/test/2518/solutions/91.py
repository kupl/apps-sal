def check(T):
    res = 0
    for h in H:
        tmp = (h - B * T + A - B - 1) // (A - B)
        if tmp <= 0:
            break
        res += tmp
    return True if res <= T else False


N, A, B = list(map(int, input().split()))
H = [int(input()) for _ in range(N)]
H.sort(reverse=True)
res = 0
left = 0
right = 10 ** 9
while right != left:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(left)
