from collections import defaultdict as dc
dic = dc(lambda: 0)
x, y = list(map(int, input().split()))
s = list(map(int, input().split()))
siv = [0] * (max(s) + 1)
ln = len(siv)
siv[1] = 1;

for n in range(2, ln):
    if siv[n] == 0:
        siv[n] = n
        for k in range(2 * n, ln, n):
            if siv[k] == 0:
                siv[k] = n


def prf(x):
    dic = dc(lambda: 0)
    while x > 1:
        d = siv[x]
        dic[siv[x]] += 1
        x //= siv[x]

    return dic


def req(dic, k):
    cur = dic
    for n in cur:
        cur[n] %= k
    for n in cur:
        cur[n] = (k - cur[n]) % k
    tot = 1
    for n in cur:
        tot *= (n**cur[n])
    return tot


def conv(x, k):
    dicc = prf(x)
    for n in dicc:
        dicc[n] %= k
    tot = 1
    for n in dicc:
        tot *= (n**dicc[n])

    return tot


res = 0
for n in s:
    re = req(prf(n), y)
    res += dic[re]
    dic[conv(n, y)] += 1

print(res)
