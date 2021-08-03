from itertools import accumulate

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
MAX = 10 ** 5

scores = [0] * (2 * MAX + 1)
for e in a:
    scores[e] += 1

acc = list(accumulate(scores))


def f(x):
    cnt = 0
    for e in a:
        cnt += n - acc[max(0, x - e - 1)]

    return cnt


l = 0
r = 2 * MAX + 1
while r - l > 1:
    mid = (l + r) // 2
    if f(mid) >= m:
        l = mid
    else:
        r = mid

scores_sum = [i * e for i, e in enumerate(scores)]
acc_sum = list(accumulate(scores_sum))
sm = sum(a)
ans = 0
cnt_sum = 0
for e in a:
    i = max(0, l - e - 1)
    cnt = n - acc[i]
    ans += e * cnt + sm - acc_sum[i]
    cnt_sum += cnt

ans -= (cnt_sum - m) * l

print(ans)
