3


def can(a, h):
    a.sort(reverse=True)
    cur = 0
    for i in range(0, len(a), 2):
        cur += a[i]
    return cur <= h


n, h = list(map(int, input().split()))
a = list(map(int, input().split()))

lt, rt = 0, n + 1
while lt < rt - 1:
    mid = (lt + rt) // 2
    if can(a[:mid], h):
        lt = mid
    else:
        rt = mid

print(lt)
