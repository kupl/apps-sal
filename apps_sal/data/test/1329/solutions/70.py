from collections import Counter
n = int(input())


def factorization(n):
    c = Counter()
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            c[i] = cnt
    if temp != 1:
        c[temp] = 1
    if len(c) == 0:
        c[n] = 1
    c[1] = 0
    return c


def isOk(c):
    ret = 1
    for _, v in c.items():
        ret *= (v + 1)
    return ret


c = Counter([])
for i in range(1, n + 1):
    c += factorization(i)

lc = [[k, v] for k, v in c.items()]

ans = 0
f75 = sum([1 for v in c.values() if v >= 74])
ans += f75
f3 = sum([1 for v in c.values() if v >= 2])
f5 = sum([1 for v in c.values() if v >= 4])
f15 = sum([1 for v in c.values() if v >= 14])
f25 = sum([1 for v in c.values() if v >= 24])
ans += f15 * (f5 - 1)
ans += f25 * (f3 - 1)
if f5 >= 2:
    ans += (f5 * (f5 - 1) // 2) * (f3 - 2)
print(ans)
