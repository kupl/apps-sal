

from bisect import bisect_right, bisect_left
import sys
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))


class cumsum1d:
    def __init__(self, ls: list):
        '''
        1次元リストを受け取る
        '''
        from itertools import accumulate
        self.ls_accum = [0] + list(accumulate(ls))

    def total(self, i, j):
        return self.ls_accum[j] - self.ls_accum[i]


N, M = read_ints()
A = read_ints()
A.sort()
A_reversed = list(reversed(A))
A_rev_acc = cumsum1d(A_reversed)


def is_ok(X):
    cnt = 0
    ans = 0
    for a in A:
        aa = X - a
        idx_reverse = N - bisect_left(A, aa)
        cnt += idx_reverse
        ans += A_rev_acc.total(0, idx_reverse) + idx_reverse * a
    return cnt >= M, ans, cnt


def meguru_bisect(ng, ok):
    '''
    define is_okと
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        flg, ans, cnt = is_ok(mid)
        if flg:
            ok = mid
            ans_true = ans
            cnt_true = cnt
        else:
            ng = mid
    return ans_true, ok, cnt_true


ans_tmp, M_th_num, M_plus_alpha_th = \
    meguru_bisect(2 * 10 ** 5 + 1, 0)
print((ans_tmp - (M_plus_alpha_th - M) * M_th_num))
