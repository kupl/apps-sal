n = int(input())
P = list(map(int, input().split()))
X = list(map(int, input().split()))

dp = [0] * n
child = [[] for i in range(n)]
for i in range(n - 1):
    child[P[i] - 1].append(i + 1)

for i in range(n - 1, -1, -1):
    if not child[i]:
        dp[i] = 0
    else:
        child_sum_min = 0
        child_sum_rest = 0
        change_candidate = set([0])  # 色を変更した場合に生じる差分を管理する
        for c in child[i]:
            z = min(X[c], dp[c])
            child_sum_min += z
        if child_sum_min > X[i]:
            print('IMPOSSIBLE')
            return
        change_space = X[i] - child_sum_min
        for c in child[i]:
            z = min(X[c], dp[c])
            rest = max(X[c], dp[c]) - z
            child_sum_rest += rest
            tmp = set(change_candidate)
            for num in change_candidate:
                if num + rest <= change_space:
                    tmp.add(num + rest)
            change_candidate = tmp
        dp[i] = child_sum_min + child_sum_rest - max(change_candidate)

print('POSSIBLE')
