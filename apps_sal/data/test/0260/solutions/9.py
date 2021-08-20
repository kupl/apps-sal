import math
(m, k) = list(map(int, input().strip(' ').split(' ')))


def solve(x):
    ans = 0
    tot = 0
    for i in reversed(list(range(int(math.log2(x) + 1)))):
        if x & 1 << i:
            ans += math.comb(i, k - tot)
            tot += 1
            if tot > k:
                return ans
    return ans


def judge(x):
    return solve(x * 2) - solve(x) >= m


(l, r) = (1, 2)
while not judge(r):
    (l, r) = (r, r * 2)
ans = -1
while l <= r:
    mid = l + r >> 1
    if judge(mid):
        (ans, r) = (mid, mid - 1)
    else:
        l = mid + 1
print(ans)
