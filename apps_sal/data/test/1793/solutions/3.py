from collections import defaultdict
import sys


def rec(n, l, s):
    # dp[i] is a doctionary, where key is the chain length
    # and value is the weight at node i
    dp = [{} for _ in range(n)]
    ans = 0
    for cur in range(n - 1, -1, -1):
        child_of_cur = children.get(cur, None)
        if not child_of_cur:
            dp[cur][1] = weight[cur]
            continue
        ans += len(child_of_cur) - 1
        cur_weight = weight[cur]
        for ch in child_of_cur:
            for ln, child_weight in dp[ch].items():
                if ln == l:
                    continue
                agg_weight = cur_weight + child_weight
                if agg_weight > s:
                    continue
                if ln + 1 not in dp[cur]:
                    dp[cur][ln + 1] = agg_weight
                dp[cur][ln + 1] = min(dp[cur][ln + 1], agg_weight)

        if not dp[cur]:
            ans += 1
            dp[cur][1] = weight[cur]

    return ans + 1


weight = []
children = defaultdict(set)
n, l, s = map(int, sys.stdin.readline().split())
for w in map(int, sys.stdin.readline().split()):
    if w > s:
        print(-1)
        return
    weight.append(w)
if n == 1:
    print(-1 if weight[0] > s else 1)
    return
for i, v in enumerate(map(int, sys.stdin.readline().split())):
    children[v - 1].add(i + 1)
print(rec(n, l, s))
