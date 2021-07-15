n,q = [int(x) for x in input().split()]

p = []

for _ in range(q):
    p.append([int(x)-1 for x  in input().split()])


def pre(ind):
    res = [0 for _ in range(n)]
    for i in range(q):
        if i == ind : continue
        res[p[i][0]] += 1
        if p[i][1] + 1 < n:
            res[p[i][1] + 1] -= 1
    t = 0
    total = 0
    for i in range(n):
        t += res[i]
        res[i] = t
        if res[i] > 0:
            total += 1
    for i in range(n):
        if res[i] > 1 : res[i] = 0
    for i in range(1,n):
        res[i] += res[i-1]
    return total,res


best = 0

for i in range(q):
    total,table = pre(i)
    for j in range(q):
        if j== i : continue
        count = table[p[j][1]]
        if p[j][0] > 0 :
            count -= table[p[j][0] - 1] 
        best = max(best,total-count)

print(best)

