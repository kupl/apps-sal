n = int(input())
a = sorted(list(map(int, input().split())))
mx = max(a)
b = []
c = []
d = []
e = []
sum1 = 0
sum2 = 0
for i in range(n):
    if a[i] >= 0:
        sum1 += a[i]
        if a[i] % 2 == 0:
            b.append(a[i])
        else:
            c.append(a[i])
    else:
        sum2 += a[i]
        if a[i] % 2 == 0:
            d.append(a[i])
        else:
            e.append(a[i])
if sum1 % 2 == 1 and sum1 > 0:
    print(sum1)
elif len(e) > 0:
    if len(c) > 0:
        print(max(sum1 + e[-1], sum1 - c[0]))
    else:
        print(sum1 + e[-1])
elif len(c) > 0:
    print(sum1 - c[0])
