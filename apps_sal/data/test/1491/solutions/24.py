n = input()
m = input().split()
a = []
b = []
for s in m:
    i = int(s)
    if int(i**(1 / 2))**2 == i:
        a.append(i)
    else:
        b.append(i)

if len(a) >= len(b):
    ans = 0
    a = sorted(a)
    for i in range(len(a) - 1, len(a) - (len(a) - len(b)) // 2 - 1, -1):
        if a[i] != 0:
            ans += 1
        else:
            ans += 2
    print(ans)

else:
    k = 0
    r = len(b) - len(a)
    r = int(r / 2)
    a = []
    for i in b:
        q = int(i**(1 / 2))
        q1 = q**2
        q2 = (q + 1)**2
        q1 = i - q1
        q2 = q2 - i
        if q1 < q2:
            q = q1
        else:
            q = q2
        a.append(q)
    print(sum(sorted(a)[:r]))
