(n, m) = list(map(int, input().split()))
xrr = [int(x) for x in input().split()]
prr = [int(x) for x in input().split()]
xrr.sort()
gcd = xrr[1] - xrr[0]
for i in range(1, n - 1):
    u = gcd
    v = xrr[i + 1] - xrr[i]
    temp = 0
    while v:
        temp = u % v
        u = v
        v = temp
    gcd = u
for i in range(m):
    if gcd % prr[i] == 0:
        print('YES')
        print(xrr[0], i + 1)
        break
else:
    print('NO')
