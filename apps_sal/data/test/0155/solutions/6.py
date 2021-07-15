n, m, k = list(map(int, input().split()))
if k < n:
    print(k+1, 1)
else:
    k = k-(n-1)
    tmp = k//(2*(m-1))
    k = k%(2*(m-1))
    x, y = n-2*tmp+1, 2
    if k > 0:
        x = x-1
        k = k-1
        if k <= m-2:
            y = y+k
        else:
            k = k-(m-1)
            x = x-1
            y = m-k
    print(x, y)

