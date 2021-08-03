from collections import Counter
n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab_s = sorted(ab, key=lambda x: x[1])
ab_r = list(reversed(ab_s))

t = [x[0] for x in ab_r]
d = [x[1] for x in ab_r]

t_set = len(set(t[:k]))
d_sum = sum(d[:k])

res = [t_set**2 + d_sum]

t_cou = Counter(t[:k])

dp = [0] * (n + 1)
j_old = k - 1

for i in t_cou:
    dp[i] = t_cou[i]

for i in range(k, n):
    t_new = ab_r[i][0]
    if dp[t_new] == 0:
        for j in range(j_old, -1, -1):
            t_old = ab_r[j][0]
            if dp[t_old] <= 1:
                pass
            else:
                dp[t_new] = 1
                dp[t_old] -= 1
                t_set += 1
                d_sum = d_sum - ab_r[j][1] + ab_r[i][1]
                res.append(t_set**2 + d_sum)
                j_old = j - 1
                break
            j_old = 0

print(max(res))
