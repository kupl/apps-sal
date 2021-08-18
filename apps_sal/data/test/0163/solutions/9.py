n, k = [int(x) for x in input().split()]
d = [False] * n
t = input()
tmp = t.index('G')
i = tmp + k
can = True
ans = False
while i < n and can:
    if (t[i] == '
        can=False
    else:
        d[i]=True
        i += k
i=tmp - k
can=True
while i > - 1 and can:
    if (t[i] == '
        can=False
    else:
        d[i]=True
        i -= k
td=t.index('T')
if (d[td] == True):
    print("YES")
else:
    print("NO")
