# list(map(int, input().split()))
n, m = list(map(int, input().split()))
ost = list(map(int, input().split()))
price = list(map(int, input().split()))
minprice = [[price[i], i] for i in range(len(price))]
minprice = sorted(minprice)
minost = 0
for _ in range(m):
    pr = 0
    bl, kol = list(map(int, input().split()))
    bl -= 1
    if (ost[bl] >= kol):
        pr = kol * price[bl]
        ost[bl] -= kol
    else:
        kol -= ost[bl]
        pr = ost[bl] * price[bl]
        ost[bl] = 0
        while(kol > 0):
            if (minost == n):
                pr = 0
                break
            minbl = minprice[minost][1]
            if (ost[minbl] >= kol):
                pr += kol * price[minbl]
                ost[minbl] -= kol
                kol = 0
            else:
                kol -= ost[minbl]
                pr += ost[minbl] * price[minbl]
                ost[minbl] = 0
                minost += 1
                if (minost == n):
                    pr = 0
                    break
    print(pr)
