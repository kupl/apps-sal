
x, k = [int(s) for s in input().split()]
a = [0]
u = [False for i in range(4001)]
k = k + 1
for i in range(1, k):
    o = [int(s) for s in input().split()]
    a.append(o[1])
    if o[0] == 1:
        u[o[1]] = True

a.append(x)
k = k + 1
a = sorted(a)
cnt1 = cnt2 = 0
for i in range(1, k):
    if u[a[i - 1]]:
        last = a[i - 1] + 1
    else:
        last = a[i - 1]
    cnt1 += (a[i] - last) >> 1
    cnt2 += a[i] - last - 1

print(cnt1, cnt2)
