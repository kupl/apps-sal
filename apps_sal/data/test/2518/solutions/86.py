N, A, B = list(map(int, input().split()))
H = []
for _ in range(N):
    H.append(int(input()))
H = sorted(H)


def check(x):
    cnt = 0
    for h in H:
        if h > x * B:
            tmp = (h - x * B) // (A - B)
            # 切り上げ
            if tmp * (A - B) != h - x * B: tmp += 1
            cnt += tmp
    if cnt <= x:
        return True
    else:
        return False
# (l,r]


def bisect(l, r):
    if r - l == 1: return r
    mid = (l + r) // 2
    if check(mid):
        return bisect(l, mid)
    else:
        return bisect(mid, r)


print((bisect(0, 10**20)))
