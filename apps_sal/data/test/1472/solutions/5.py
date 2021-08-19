from collections import defaultdict
ans = defaultdict(int)
(N, X, Y) = map(int, input().split())
for i in range(1, N + 1):
    for j in range(1 + i, N + 1):
        l1 = j - i
        l2 = abs(X - i) + 1 + abs(Y - j)
        ans[min(l1, l2)] += 1
for i in range(1, N):
    print(ans[i])
