import collections
a = int(input())
b = [int(s) for s in input().split()]
b = sorted(b)
mod = int(1000000)
d = {}
e = collections.Counter(b)
X = int(0)
ans = int(0)

for i in range(a):
    if d.get(b[i]) == None:
        if e.get(b[i]) != 1:
            d[b[i]] = 1
        X = b[i]
        while X <= (mod - b[i]):
            X += b[i]
            d[X] = 1
        X = 0
    else:
        pass

for i in range(a):
    if d.get(b[i]) == None:
        ans += 1

print(ans)
