from bisect import bisect_left
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()


def get_count(tot):
    '''
    tot以上を満たす幸福度の握手の個数を数える
    '''
    ret = 0
    for i in range(N):
        cnt = bisect_left(A, tot - A[i])
        ret += N - cnt
    return ret


# 右からの累積和
Asum = A[:]
for i in range(N - 2, -1, -1):
    Asum[i] += Asum[i + 1]


def get_sum(tot):
    '''
    左端を固定した時の右端の個数分だけ左端を足し、右端の区間和（累積和）も足す。
    '''
    ret = 0
    for i in range(N):
        idx = bisect_left(A, tot - A[i])
        cnt = N - idx
        ret += A[i] * cnt
        # print(idx)
        if idx == N:
            continue
        ret += Asum[idx]
        # print(f'ret = {ret}')
    return ret


# M回握手できる上限を求める
ok = 0
ng = 10**12
while ok + 1 != ng:
    md = (ok + ng) // 2
    if M <= get_count(md):
        ok = md
    else:
        ng = md
# print(ok)
# print(get_sum(ok+1))
# print(M - get_count(ok+1))
# print(Asum)
ans = get_sum(ok + 1) + (M - get_count(ok + 1)) * ok

print(ans)
