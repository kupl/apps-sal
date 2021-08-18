import math
N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]

x = A - B


def func(cnt):
    dmg = B * cnt
    tmp = [max(0, val - dmg) for val in h]
    cnt2 = sum([math.ceil(val / x) for val in tmp])
    if cnt2 > cnt:
        return False
    else:
        return True


ok = 10**9
ng = 0
while abs(ok - ng) > 1:
    cnt = (ok + ng) // 2
    if func(cnt):
        ok = cnt
    else:
        ng = cnt
print(ok)
