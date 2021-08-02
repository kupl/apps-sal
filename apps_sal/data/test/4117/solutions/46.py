import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]


N = ri()
L = ri_()


def f(L):
    L_ = sorted(L)
    return len(set(L_)) == 3 and L_[0] + L_[1] > L_[2]


ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if f([L[i], L[j], L[k]]):
                ans += 1
print(ans)
