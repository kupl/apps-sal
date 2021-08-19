def factorize(x):
    tmp = x
    cnt = 0
    while tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    return (tmp, cnt)


n = int(input())
for i in range(n):
    k = int(input())
    x = dict()
    cnt = 0
    tmp = list(map(int, input().split()))
    for j in tmp:
        (g, v) = factorize(j)
        try:
            x[g] = max(x[g], v)
        except:
            x[g] = v
    for c in list(x.keys()):
        cnt += x[c]
    print(cnt)
