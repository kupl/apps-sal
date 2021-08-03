n, k, m = list(map(int, input().split()))
lang = input().split()
cost = list(map(int, input().split()))

groups = {}
mincost = {}

for g in range(k):
    x, *ind = list(map(int, input().split()))
    for index in ind:
        groups[lang[index - 1]] = g + 1
    m = 10000000000
    for index in ind:
        if cost[index - 1] < m:
            m = cost[index - 1]
    mincost[g + 1] = m

message = input().split()

total = 0

for word in message:
    total += mincost[groups[word]]

print(total)
