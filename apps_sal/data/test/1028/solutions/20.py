n, m = map(int, input().split())
if n == m:
    print(0, 0)
elif n == m+1:
    print(1, 1)
else:
    p = n-m+1
    maxi = p*(p-1)//2
    d = n//m
    if d == 1:
        mini = n - m
    else:
        if n % m:
            d += 1
            remain = d*m-n
            mini = (d-1)*(d-2)//2*remain
            remain = n - remain*(d-1)
            remain //= d
            mini += d*(d-1)//2*remain
        else:
            mini = d*(d-1)//2*m
    print(mini, maxi)
