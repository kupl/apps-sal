import sys


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


N = ir()
S = sr()


def check(x):
    candidate = set()
    for i in range(N - 2 * x + 1):
        candidate.add(S[i:i + x])
        if S[i + x:i + 2 * x] in candidate:
            return True
    return False


ok = 0
ng = N
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
