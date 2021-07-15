n = int(input())
a = list(map(int, input().split()))
f1 = s1 = f2 = s2 = 0
for i in range(len(a)):
    if i % 2 == 0:
        f2 += a[i]
    else:
        s2 += a[i]
res = 0
z = (n - 1) % 2
for i in range(len(a)):
    if i % 2 == 0:
        f2 -= a[i]
        if f2 + s1 == s2 + f1:
            res += 1
        f1 += a[i]
    else:
        s2 -= a[i]
        if f2 + s1 == s2 + f1:
            res += 1
        s1 += a[i]
print(res)
