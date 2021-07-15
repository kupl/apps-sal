n = int(input())

cs = []
vs = []

for i in range(n):
    c, v = input().split(' ')
    c = int(c)

    cs += [c]
    vs += [set(v)]

BigInt = 10 ** 10
ans = BigInt

for opt in ['A|B|C', 'AB|C', 'AC|B', 'BC|A', 'ABC']:
    opt = [set(s) for s in opt.split('|')]
    cur = 0

    for group in opt:
        minCost = BigInt

        for c, v in zip(cs, vs):
            if v.issuperset(group) and c < minCost:
                minCost = c

        if minCost == BigInt:
            cur = BigInt
            break

        cur += minCost

    if cur < ans:
        ans = cur

    #print(opt, cur)
    
print(-1 if ans == BigInt else ans)
