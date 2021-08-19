n = int(input())
a = list(map(int, input().split()))
n = 0
p = 0
cn = 0
cp = 0
for i in a:
    if i < 0:
        (cn, cp) = (cp, cn)
        cn += 1
    else:
        cp += 1
    n += cn
    p += cp
print(n, p)
