(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
dic = {}
wk = 1
start = 0
for i in range(1, n + 1):
    wk = a[wk - 1]
    if wk in dic:
        start = dic[wk]
        break
    dic[wk] = i
end = len(dic)
loopcnt = end - start + 1
keys = list(dic.keys())
if k < start:
    print(keys[k - 1])
else:
    chk = (k - start + 1) % loopcnt
    if chk == 0:
        chk = loopcnt
    print(keys[start - 1 + chk - 1])
