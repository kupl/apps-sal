import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
cmb = 0
for x in c.values():
    cmb += x * (x - 1) // 2
for z in a:
    y = c.get(z)
    before = y * (y - 1) // 2
    after = (y - 1) * (y - 2) // 2
    ans = cmb - before + after
    print(ans)
