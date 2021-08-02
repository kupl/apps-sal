import bisect
import sys
readline = sys.stdin.readline

N, M = list(map(int, readline().split()))
A = sorted(list(map(int, readline().split())))

sumA = [0] + A.copy()
for i in range(1, len(sumA)):
    sumA[i] += sumA[i - 1]

# 左手34,33,19,14,10
# 右手34,33,19,14,10
# X以上の握手をできる組だけ採用する
# 例：50以上の握手をできるのは、
# 左手34に対しては34,33,19
# 右手33に対しては34,33,19
# この合計がM回を越えると採用できない。
# M回を下回る場合は、すべての握手の合計で最大値を更新

ok = -1
ng = 10 ** 5 * 2 + 1


def isOk(x):
    # x以上の握手だけ採用するとき、採用できる場合に全体の合計点はいくつになるか
    cnt = 0
    for left in A:
        right = x - left
        ind = bisect.bisect_left(A, right)
        cnt += N - ind
    if cnt > M:
        return True
    else:
        return False


while abs(ng - ok) > 1:
    mid = abs(ng + ok) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

# ok以上の握手だけ許容する場合の点数を算出
ans = 0
num = 0
for left in A:
    right = ok - left
    ind = bisect.bisect_left(A, right)
    ans += sumA[-1] - sumA[ind] + (N - ind) * left
    num += N - ind

if num > M:
    ans -= (num - M) * ok

print(ans)
