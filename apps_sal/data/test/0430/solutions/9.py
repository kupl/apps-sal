n = int(input().strip())
a = list(map(int, input().split()))
k = sum(a) / 2
if k == int(k):
    k = int(k)
    f = [0] * (k + 1)
    f[0] = 1
    for i in range(len(a)):
        f_n = f[:]
        for z in range(a[i], k + 1):
            if f[z - a[i]] == 1:
                f_n[z] = 1
        f = f_n
    print('YES' if f[k] == 1 else 'NO')
else:
    print('NO')
