n, k = list(map(int, input().split()))
c = 1
z = 1
ok = 1

for i in range(1, k + 1):
    c = z
    while z % i != 0:
        z += c
    if z > n + 10:
        ok = 0
        break
if (n + 1) % z == 0 and ok:
    print('Yes')
else:
    print('No')
