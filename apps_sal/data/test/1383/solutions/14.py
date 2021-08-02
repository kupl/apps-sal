n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
da = {}
db = {}
for i in a:
    da[i] = da.get(i, 0) + 1
for i in b:
    db[i] = db.get(i, 0) + 1
x = 1000000001
ca = {}
cb = {}
for i in da:
    try:
        ca[da[i]].append(i)
    except:
        ca[da[i]] = [i]
for i in db:
    try:
        cb[db[i]].append(i)
    except:
        cb[db[i]] = [i]
ans = {}
for i in ca:
    for j in ca[i]:
        for k in cb[i]:
            ans[(k - j) % m] = ans.get((k - j) % m, 0) + 1
l = len(da)
for i in ans:
    if ans[i] == l:
        x = min(x, i)
print(x)
