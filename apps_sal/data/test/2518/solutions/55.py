import math
n, a, b = list(map(int, input().split()))
h_list = [int(input()) for _ in range(n)]

lb = 0
ub = 10**9


def is_ok(m):
    tmp_ans = 0
    for h in h_list:
        tmp_h = max(h - m * b, 0)
        tmp_ans += math.ceil(tmp_h / (a - b))
    if tmp_ans <= m:
        return True
    else:
        return False


ng = lb
ok = ub + 1
while ok - ng > 1:
    m = (ok + ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m

print(ok)
