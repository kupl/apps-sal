import sys
readline = sys.stdin.readline

N, A, B = map(int, readline().split())
H = [int(readline()) for i in range(N)]


A -= B

ng = 0
ok = 10 ** 9


def isOk(x):
    cnt = 0
    for i in range(len(H)):
        h = H[i] - x * B
        if h > 0:
            cnt += (h + A - 1) // A
    return cnt <= x


while abs(ok - ng) > 1:
    mid = abs(ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ok)
