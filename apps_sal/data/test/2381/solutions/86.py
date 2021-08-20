mod = 10 ** 9 + 7
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
neg = []
zero = 0
pos = []
for a in A:
    if a < 0:
        neg.append(a)
    else:
        pos.append(a)
pos.sort()
neg.sort(reverse=True)
if len(pos) == 0:
    res = 1
    if K % 2 == 0:
        neg.reverse()
    for a in neg[:K]:
        res *= a
        res %= mod
else:
    res = 1
    if K % 2 == 1:
        res = pos.pop()
        K -= 1
    while K > 1 and len(pos) > 1 and (len(neg) > 1):
        if pos[-1] * pos[-2] > neg[-1] * neg[-2]:
            res *= pos.pop()
            res %= mod
            res *= pos.pop()
            res %= mod
        else:
            res *= neg.pop()
            res %= mod
            res *= neg.pop()
            res %= mod
        K -= 2
    while K > 1 and len(pos) > 1:
        res *= pos.pop()
        res %= mod
        res *= pos.pop()
        res %= mod
        K -= 2
    while K > 1 and len(neg) > 1:
        res *= neg.pop()
        res %= mod
        res *= neg.pop()
        res %= mod
        K -= 2
    while K and pos:
        res *= pos.pop()
        res %= mod
        K -= 1
    while K and neg:
        res *= neg.pop()
        res %= mod
        K -= 1
print(res)
