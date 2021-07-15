n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aa = [0 for i in range(5)]
bb = [0 for i in range(5)]
cc = [0 for i in range(5)]
for i in range(n):
    aa[a[i] - 1] += 1
    cc[a[i] - 1] += 1
for i in range(n):
    bb[b[i] - 1] += 1
    cc[b[i] - 1] += 1
f = True
for i in range(5):
    if cc[i] % 2 != 0:
        f = False
        break
    else:
        cc[i] //= 2
if not f:
    print(-1)
else:
    o = 0
    for i in range(5):
        o += abs(cc[i] - aa[i])
    print(o // 2)

