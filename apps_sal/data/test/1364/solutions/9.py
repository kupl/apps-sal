n = int(input())
a = list(map(int, input().split()))
res = 2
d = []
c = a[0]
cc = 1
for i in range(1, n):
    if c == a[i]:
        cc += 1
    else:
        d.append(cc)
        c = a[i]
        cc = 1
d.append(cc)
ma = 0
for i in range(1, len(d)):
    ma = max(ma, min(d[i], d[i - 1]))
print(ma * 2)
