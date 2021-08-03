list_keys = ['A', 'B', 'C', 'AB', 'BC', 'AC', 'ABC', '1', '2']


def sortStr(s):
    res = ''
    s = sorted(s)
    for c in s:
        res += c
    return res


def check(s1, s2, s3):
    s = s1 + s2 + s3
    return 'A' in s and 'B' in s and 'C' in s


val = {}
INF = 1e9
for key in list_keys:
    val[key] = INF
val['1'] = 0
val['2'] = 0

n = int(input())
for i in range(n):
    v, s = input().split()
    v = int(v)
    s = sortStr(s)
    if val[s] > v:
        val[s] = v

res = INF
for key1 in list_keys:
    for key2 in list_keys:
        for key3 in list_keys:
            if check(key1, key2, key3):
                res = min(res, val[key1] + val[key2] + val[key3])

if res == INF:
    res = -1
print(res)
