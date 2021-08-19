(n, l) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
aa = [0] * n
bb = [0] * n
aa[0] = l - a[-1] + a[0]
bb[0] = l - b[-1] + b[0]
for i in range(1, n):
    aa[i] = a[i] - a[i - 1]
    bb[i] = b[i] - b[i - 1]
for i in range(n):
    if aa == bb:
        print('YES')
        break
    aa.append(aa[0])
    aa.pop(0)
else:
    print('NO')
