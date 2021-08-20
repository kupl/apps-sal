n = int(input())
lista = []
xy = []
for i in range(n):
    a = int(input())
    lista.append(a)
    s = [list(map(int, input().split())) for _ in range(a)]
    xy.append(s)
ans = 0
for j in range(2 ** n):
    num = 0
    d = []
    for k in range(n):
        if j >> k & 1 == 1:
            d.append(1)
        else:
            d.append(0)
    c = 0
    for l in range(n):
        cnt = 0
        if d[l] == 1:
            if lista[l] != 0:
                for m in range(lista[l]):
                    if xy[l][m][1] == d[xy[l][m][0] - 1]:
                        cnt += 1
                        if cnt == lista[l]:
                            c += 1
                    else:
                        break
            else:
                c += 1
    if c == d.count(1):
        num = c
    ans = max(num, ans)
print(ans)
