import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

#二分探索
N = ir()
S = sr()

def check(x):
    # x文字右側にずらした場所を調べる
    candidate = set()
    for i in range(N - 2*x + 1):
        candidate.add(S[i:i+x])
        if S[i+x:i+2*x] in candidate:
            return True
    return False

ok = 0; ng = N
while abs(ng-ok) > 1:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)

