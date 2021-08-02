c, d = list(map(int, input().split()))
n, m = list(map(int, input().split()))
k = int(input())
need = n * m - k
if need <= 0:
    print(0)
else:
    r1 = c / n
    if r1 < d:
        div, rest = divmod(need, n)
        cont = div * c
        cont += min(c, d * rest)
        print(max(0, cont))
    else:
        print(need * d)
