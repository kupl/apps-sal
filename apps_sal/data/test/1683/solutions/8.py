from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter()

for ai in a:
    l = len(str(ai))
    c[l] += 1

res = 0
mod = 998244353

for ai in a:
    s = str(ai)
    l = len(s)
    for key, value in c.items():
        if key >= l:
            eq = '0'.join(s)
            res = (res + int(eq)*value)%mod
            eq = '0'.join(s) + '0'
            res = (res + int(eq) * value) % mod
        else:
            eq = []
            for i in range(l-key, l):
                eq.append(s[i]*2)
            eq = [s[:-key]] + eq
            eq = ''.join(eq)
            res = (res + (int(eq) + int(s[:-key]+'0'*2*key)) * value) % mod

print(res)
