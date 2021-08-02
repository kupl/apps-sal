import sys
readline = sys.stdin.readline


def calc(x):
    if x == 0:
        return 0
    ng = 0
    ok = 10**5
    while abs(ok - ng) > 1:
        med = (ok + ng) // 2
        S = med * (med + 1) // 2
        if abs(x) <= S:
            ok = med
        else:
            ng = med
    for i in range(5):
        if (ok + i) * (ok + 1 + i) // 2 % 2 == x % 2:
            break

    return ok + i


T = int(readline())
Ans = [None] * T
for qu in range(T):
    a, b = map(int, readline().split())
    Ans[qu] = calc(a - b)
print('\n'.join(map(str, Ans)))
