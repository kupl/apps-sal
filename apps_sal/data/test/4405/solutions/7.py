n = list(map(int, input().split()))
a = list(map(int, input().strip().split()))
alla = {}
for x in a:
    if alla.get(x) == None:
        alla.update({x: 0})
    alla.update({x: alla[x] + 1})
als = set(a)
res = []
for x in als:
    res.append(alla[x])
res.sort()
n = len(res)
ans = 0
for i in range(1, res[n - 1] + 1):
    curs = i
    cur = i
    ans = max(ans, curs)
    j = n - 2
    if cur % 2 == 1:
        continue
    cur = cur // 2
    while j >= 0 and res[j] >= cur:
        curs += cur
        ans = max(ans, curs)
        j -= 1
        if cur % 2 != 0:
            break
        cur = cur // 2
print(ans)
