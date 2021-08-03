n = int(input())
s = list(map(lambda x: int(x), input().split()))
a = {}
for i in range(n):
    if s[i] in a:
        a[s[i]] += 1
    else:
        a[s[i]] = 1

m = int(input())

b = list(map(lambda x: int(x), input().split()))
c = list(map(lambda x: int(x), input().split()))

ans = -1
d = -1
pd = -1

for i in range(m):
    if b[i] in a:
        cd = a[b[i]]
    else:
        cd = 0

    if c[i] in a:
        cpd = a[c[i]]
    else:
        cpd = 0

    if (cd > d) or (cd == d and cpd > pd):
        ans = i
        d = cd
        pd = cpd

print(ans + 1)
