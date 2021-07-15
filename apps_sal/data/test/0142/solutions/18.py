n, lit = list(map(int, input().split()))
cost = list(map(int, input().split())) + ([1 << 100] * 33)
n = len(cost)
rlit = lit

for i in range(n):
    for j in range(i-1, -1, -1):
        cost[i] = min(cost[i], cost[j] * (1 << (i - j)))

res = 0

for i in range(n):
    if (1 << i) & lit:
        res += cost[i]

b = []

while lit:
    b.append(lit % 2)
    lit //= 2

rres = res

for i in range(len(b)-1, -1, -1):
    if b[i] == 1:
        for j in range(i-1, -1, -1):
            if b[j] == 0:
                add = cost[j]
                sub = 0
                for k in range(j-1, -1, -1):
                    if b[k] == 1:
                        sub += cost[k]
                res = min(res, rres+add-sub)

for i in range(n):
    if (1 << i) > rlit and cost[i] < res:
        res = cost[i]

print(res)

