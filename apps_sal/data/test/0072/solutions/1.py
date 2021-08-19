from collections import Counter
n = int(input().strip())
names = ['Kuro', 'Shiro', 'Katie']
ss = {}
for name in names:
    ss[name] = input().strip()


def beauty(s, n):
    cm = Counter(s).most_common(1)[0][1]
    if n == 1 and cm == len(s):
        return cm - 1
    else:
        return min(len(s), cm + n)


res = {}
for name in names:
    res[name] = beauty(ss[name], n)
bestv = max(res.values())
if list(res.values()).count(bestv) > 1:
    print('Draw')
else:
    for (name, v) in list(res.items()):
        if v == bestv:
            print(name)
