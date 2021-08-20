import collections
import bisect


def solve1(dp):
    count = 0
    for num in dp.values():
        n = len(num)
        if n >= 3:
            count += n * (n - 1) * (n - 2) // 6
    return count


def solve(n, k, As, dp):
    count = 0
    for (i, ak) in enumerate(As):
        if ak % k:
            continue
        if ak == 0:
            continue
        a = ak // k
        akk = ak * k
        n_left = bisect.bisect_left(dp[a], i)
        n_right = len(dp[akk]) - bisect.bisect_left(dp[akk], i)
        count += n_left * n_right
    n0 = len(dp[0])
    if n0 >= 3:
        count += n0 * (n0 - 1) * (n0 - 2) // 6
    return count


(n, k) = map(int, input().split())
As = list(map(int, input().split()))
dp = collections.defaultdict(list)
for (i, a) in enumerate(As):
    dp[a].append(i)
if n < 3:
    print(0)
elif k == 1:
    print(solve1(dp))
else:
    print(solve(n, k, As, dp))
