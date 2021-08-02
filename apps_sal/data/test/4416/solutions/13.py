n, k = map(int, input().split())
ablike = []
alike = []
blike = []
for i in range(n):
    t, a, b = map(int, input().split())
    if a == 1 and b == 1:
        ablike.append(t)
    elif a == 1:
        alike.append(t)
    elif b == 1:
        blike.append(t)
ablike.sort()
abtot = len(ablike)
alike.sort()
atot = len(alike)
blike.sort()
btot = len(blike)
x = min(atot, btot)
if abtot + x < k:
    print(-1)
else:
    p = k
    i = 0
    j = 0
    tot = 0
    while p > 0:
        if j < abtot and i < x:
            if ablike[j] <= (alike[i] + blike[i]):
                tot = tot + ablike[j]
                j = j + 1
                p = p - 1
            else:
                tot = tot + alike[i] + blike[i]
                i = i + 1
                p = p - 1
        elif j < abtot:
            tot = tot + ablike[j]
            j = j + 1
            p = p - 1
        else:
            tot = tot + alike[i] + blike[i]
            i = i + 1
            p = p - 1
    print(tot)
