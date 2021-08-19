import sys


def rs():
    return sys.stdin.readline().rstrip()


def ri():
    return int(rs())


def rs_():
    return [_ for _ in rs().split()]


def ri_():
    return [int(_) for _ in rs().split()]


N = ri()
A = ri_()
ans = 0
tmp = A[0]
for i in range(1, N):
    if tmp > A[i]:
        ans += tmp - A[i]
    else:
        tmp = A[i]
print(ans)
