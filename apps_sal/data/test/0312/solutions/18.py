n, m = list(map(int,input().split()))
if n != 1:
    if n % 2 == 0:
        if n // 2 >= m:
            print(m+1)
        else:
            print(m-1)
    else:
        n -= 1
        if n // 2 >= m:
            print(m+1)
        else:
            print(m-1)
else:
    print(1)

