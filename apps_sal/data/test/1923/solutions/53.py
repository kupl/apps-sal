a = int(input())
b = list(map(int, input().split()))
c = sorted(b, reverse=True)
d = 0
'e.append(c[0])\ne.append(c[1])\ndel c[0]\ndel c[1]'
for i in range(a):
    f = 2 * i
    g = 2 * i + 1
    if c[f] == c[g]:
        d += c[g]
    else:
        d += c[g]
print(d)
