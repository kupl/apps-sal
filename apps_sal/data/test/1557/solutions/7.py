h1, a1, c1 = [int(i) for i in input().split()]
h2, a2 = [int(i) for i in input().split()]
n = 0
a = []
while h2 > 0:
    if h2 <= a1:
        a.append('STRIKE')
        h2 -= a1
    else:
        if h1 > a2:
            a.append('STRIKE')
            h2 -= a1
        else:
            a.append('HEAL')
            h1 += c1
        if h2 > 0:
            h1 -= a2
    n += 1
print(n)
for i in a:
    print(i)

