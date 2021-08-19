# reference: https://www.onakasuitacity.com/abc144-f/

import numpy as np

n, m = map(int, input().split())
outgoing = [[] for _ in range(n)]
incoming = [[] for _ in range(n)]
for _ in range(m):
    si, ti = map(int, input().split())
    outgoing[si - 1].append(ti - 1)
    incoming[ti - 1].append(si - 1)


ex_dp = np.zeros(n)
for v in reversed(range(n - 1)):   # O(m)
    outgoing_degree = len(outgoing[v])
    ex_dp[v] = 1 + sum(ex_dp[post] for post in outgoing[v]) / outgoing_degree if outgoing_degree != 0 else np.inf

p_dp = np.ones(n)
for v in range(1, n):      # O(m)
    p_dp[v] = sum(p_dp[prev] / len(outgoing[prev]) for prev in incoming[v])

min_ex = ex_dp[0]
for v, posts in enumerate(outgoing):      # O(m)
    outgoing_degree = len(outgoing[v])
    if outgoing_degree <= 1:
        continue

    max_post = max(posts, key=lambda pos: ex_dp[pos])
    diff_v_ex = 0
    for w in posts:
        if w == max_post:
            diff_v_ex -= 1 / outgoing_degree * ex_dp[w]
        else:
            diff_v_ex += 1 / (outgoing_degree * (outgoing_degree - 1)) * ex_dp[w]
    min_ex = min(ex_dp[0] + p_dp[v] * diff_v_ex, min_ex)

print(min_ex)
