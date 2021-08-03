n, a, b = list(map(int, input().split()))
H = [int(input()) for _ in range(n)]


def ok(x):
    cnt = 0
    for h in H:
        cnt += max(0, (h - b * x - 1) // (a - b) + 1)
    return cnt <= x


top = 10**9
bottom = 0
while top - bottom > 1:
    mid = (top + bottom) // 2
    if ok(mid):
        top = mid
    else:
        bottom = mid
print(top)
