n = int(input())
colors = list(map(int, input().split()))
cnt = [0 for _ in range(100001)]
vals = dict()
ind = 1
for i in range(n):
    el = colors[i]
    if cnt[el] != 0:
        vals[cnt[el]] -= 1
        if vals[cnt[el]] == 0:
            del vals[cnt[el]]
    cnt[el] += 1
    if cnt[el] in vals:
        vals[cnt[el]] += 1
    else:
        vals[cnt[el]] = 1
    if len(vals) == 2:
        tmp = list(vals.keys())
        tmp.sort()
        if tmp[0] == 1 and vals[tmp[0]] == 1 or (tmp[1] - tmp[0] == 1 and vals[tmp[1]] == 1):
            ind = i
    elif len(vals) == 1 and list(vals.keys())[0] == 1:
        ind = i
if cnt[colors[0]] == n:
    print(n)
else:
    print(ind + 1)
