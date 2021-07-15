import collections
N ,K = map(int,input().split())
lsA = list(map(int,input().split()))
counterA = collections.Counter(lsA)
valu = list(counterA.values())
valu.sort()
kind = len(set(lsA))
if kind <= K:
    ans = 0
else:
    ans = sum(valu[:kind - K])
print(ans)
