(n, m) = list(map(int, input().split()))
dic = {}
isOK = False
for i in range(m):
    (a, b) = list(map(int, input().split()))
    if a in [1, n]:
        dic.setdefault(b, 0)
        dic[b] += 1
        if dic[b] == 2:
            isOK = True
            break
    elif b in [1, n]:
        dic.setdefault(a, 0)
        dic[a] += 1
        if dic[a] == 2:
            isOK = True
            break
if isOK:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
