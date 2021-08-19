from collections import defaultdict
(N, M) = map(int, input().split())
H = list(map(int, input().split()))
edge = defaultdict(list)
for i in range(M):
    (a, b) = map(int, input().split())
    edge[a - 1].append(H[b - 1])
    edge[b - 1].append(H[a - 1])
ans = 0
for i in range(N):
    if len(edge[i]) == 0 or H[i] > max(edge[i]):
        ans += 1
print(ans)
