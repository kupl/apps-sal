(N, M, X) = map(int, input().split())
c = []
a = []
for i in range(N):
    (c_temp, *a_temp) = list(map(int, input().split()))
    c.append(c_temp)
    a.append(a_temp)
price_min = 10000000
for i in range(2 ** N):
    price_total = 0
    learn_total = [0] * M
    for j in range(N):
        if i >> j & 1:
            price_total += c[j]
            learn = a[j]
            for (k, la) in enumerate(learn):
                learn_total[k] += la
    if all((learn_total[k] >= X for k in range(M))):
        if price_min > price_total:
            price_min = price_total
if price_min == 10000000:
    print(-1)
else:
    print(price_min)
