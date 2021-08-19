(n, m, k) = (int(i) for i in input().split())
cost = sorted([int(i) for i in input().split()])[:k] + [0]
discount = [0] * n
for i in range(m):
    (a, b) = (int(j) for j in input().split())
    discount[a - 1] = max(discount[a - 1], b)
S = [0] * (k + 1)
for i in range(k):
    S[i] = cost[i] + S[i - 1]
    cost[i] += cost[i - 1]
    for j in range(i + 1):
        S[i] = min(S[i], S[j - 1] + cost[i] - cost[j - 1 + discount[i - j]])
print(S[k - 1])
