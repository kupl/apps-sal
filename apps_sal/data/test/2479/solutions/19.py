n, q = map(int, input().split())

ans = (n - 2)**2
rm = n
um = n
ruse = [-1] * (n + 1)
uuse = [-1] * (n + 1)

for _ in range(q):
    a, x = map(int, input().split())
    if a == 1:
        if uuse[x] >= 0:
            ans -= uuse[x] - 2
        else:
            dif = um - 2
            ans -= dif
            for i in range(x, n + 1):
                if uuse[i] >= 0:
                    break
                uuse[i] = um
            rm = min(rm, x)
    else:
        if ruse[x] >= 0:
            ans -= ruse[x] - 2
        else:
            dif = rm - 2
            ans -= dif
            for i in range(x, n + 1):
                if ruse[i] >= 0:
                    break
                ruse[i] = rm
            um = min(um, x)
print(ans)
