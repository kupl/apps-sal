(n, k) = input().split()
k = int(k)
l = list(n)
u = len(l)
d = '0'
i = 0
while k > 0 and i < u - 1:
    c = i + k
    if c > u:
        c = u
    d = max(l[i + 1:c + 1])
    if d > l[i]:
        j = False
        p = i + 1
        while not j:
            if l[p] == d:
                j = p
            else:
                p += 1
        for h in range(j, i, -1):
            (l[h], l[h - 1]) = (l[h - 1], l[h])
            k -= 1
        i = 0
    else:
        i += 1
x = ''
for i in l:
    x = x + str(i)
print(x)
