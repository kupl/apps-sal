N, M = list(map(int, input().split()))
abc = []
for _ in range(M):
    abc.append(list(map(int, input().split())))

cost = [-float('inf')] * N
cost[0] = 0

for i in range(2):
    for a, b, c in abc:
        a, b = a - 1, b - 1
        cost[b] = max(cost[b], cost[a] + c)

    if i == 0:
        ans = cost[N - 1]
    else:
        Max = cost[N - 1]


if ans != Max:
    print('inf')
else:
    print(ans)
