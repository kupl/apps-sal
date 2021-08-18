n, m = map(int, input().split())
a = [int(s) for s in input().split()]
c = [int(s) for s in input().split()]
types = dict()
for i in range(n):
    types[i] = c[i]
types = sorted(types.items(), key=lambda kv: kv[1])
min_c = types[0]
ind = 0
for i in range(m):
    t, d = map(int, input().split())
    t -= 1
    summ = 0
    if a[t] < d:
        summ += a[t] * c[t]
        d -= a[t]
        a[t] = 0
        while a[min_c[0]] < d:
            summ += a[min_c[0]] * c[min_c[0]]
            d -= a[min_c[0]]
            a[min_c[0]] = 0
            ind += 1
            if ind >= n:
                summ = 0
                ind -= 1
                break
            else:
                min_c = types[ind]
        else:
            summ += d * c[min_c[0]]
            a[min_c[0]] -= d
    else:
        summ += d * c[t]
        a[t] -= d
    print(summ)
