t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    k = sorted(l)
    c = min(l)
    f = 0
    for j in range(n):
        if (l[j] % c != 0):
            if (l[j] != k[j]):
                print('NO')
                f = 1
                break
    if (f == 0):
        print('YES')

