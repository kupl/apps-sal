n = int(input())
a = [0] + list(map(int, input().split()))
alive = [1 for i in range(n + 1)]
sol = sum(a)
while True:
    pot = []
    change = False
    for i in range(n, 0, -1):
        if a[i] >= 0 or alive[i] == 0:
            continue
        saldo = 0
        j = i
        while j <= n:
            saldo += alive[j] * a[j]
            j += i
        if saldo > 0:
            pot.append(i)
            continue
        change = True
        sol -= saldo
        j = i
        while j <= n:
            alive[j] = 0
            j += i
    if change:
        continue
    k = len(pot)
    for i in range(k):
        if change: break
        for j in range(i):
            saldo = 0
            for v in range(1, n + 1):
                if v % pot[i] == 0 or v % pot[j] == 0:
                    saldo += alive[v] * a[v]
            if saldo <= 0:
                change = True
                sol -= saldo
                for v in range(1, n + 1):
                    if v % pot[i] == 0 or v % pot[j] == 0:
                        alive[v] = 0
                break
    if not change:
        break
print(sol)
