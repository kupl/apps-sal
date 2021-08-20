def getUsefulWeight(coef, uw):
    if coef == 1:
        print(-1)
        return
    uw += uw / (coef - 1)
    return uw


(n, x) = list(map(int, input().strip().split(' ')))
a = list(map(int, input().strip().split(' ')))
d = {}
ret = 3
for y in a:
    val = y & x
    if y in d:
        newc = d[y]
        if ret > newc:
            ret = newc
    if val in d:
        newc = d[val] + 1
        if ret > newc:
            ret = newc
    d[y] = 0
    if val not in d:
        d[val] = 1
if ret == 3:
    print('-1')
else:
    print(ret)
