n, m = list(map(int, input().split(' ')))
aa = list(map(int, input().split(' ')))

def countMoreLess(vs, value):
    #print(vs)
    cur = 0
    res = { cur: 1 }

    for v in vs:
        cur += 1 if v > value else -1
        res[cur] = res.get(cur, 0) + 1
    #print(res)
    return res

pos = aa.index(m)

leftCounts = countMoreLess(list(reversed(aa[0:pos])), m)
rightCounts = countMoreLess(aa[pos+1:], m)

res = 0
for dif, count in list(leftCounts.items()):
    res += count * rightCounts.get(-dif, 0)
    res += count * rightCounts.get(-dif+1, 0)

print(res)

