symb = ["
inf = float("inf")


def isAlpha(char):
    return 97 <= ord(char) <= 122


def first(s):
    l = len(s)
    alpha = inf
    d = inf
    sym = inf
    for i in range(l):
        c = s[i]
        if isAlpha(c):
            alpha = min(alpha, i)
        if c.isdigit():
            d = min(d, i)
        if c in symb:
            sym = min(sym, i)

    for i in range(1, l + 1):
        c = s[l - i]
        if isAlpha(c):
            alpha = min(alpha, i)
        if c.isdigit():
            d = min(d, i)
        if c in symb:
            sym = min(sym, i)

    return [alpha, d, sym]


n, m = [int(item) for item in input().split()]
ans = float("inf")
s = []
for i in range(n):
    s.append(input())

firsts = []
for i in range(n):
    firsts.append(first(s[i]) + [i])

a = sorted(firsts, key=lambda x: x[0])
b=sorted(firsts, key=lambda x: x[1])
c=sorted(firsts, key=lambda x: x[2])

for i in range(min(m, 3)):
    for j in range(min(m, 3)):
        for k in range(min(m, 3)):
            if a[i][3] != b[j][3] and a[i][3] != c[k][3] and b[j][3] != c[k][3]:
                ans=min(ans, a[i][0] + b[j][1] + c[k][2])


print(ans)
