(n, m, k, l) = map(int, input().split())
need = k + l
if need % m == 0 and need <= n:
    print(need // m)
else:
    x = need // m + 1
    if x * m > n:
        print(-1)
    else:
        print(x)
