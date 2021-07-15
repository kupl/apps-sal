A = list(map(int, input().split()))

x = A[0]
y = A[1]
k = A[2]

if (x+y)%2 == 1 and k == -1:
    print("0")
else:
    if x > y:
        z = x
        x = y
        y = z
    if x == 1:
        print("1")
    else:
        start = (x-1)*(x-1)
        dif = y-x;
        start = start + (dif*(x-1))
        p = 1000000007
        res = 1
        x = 2
        y = start
        while y > 0:
            if (y%2 == 1):
                res = (res * x) % p
            y = y // 2
            x = (x*x) % p
        print(res)
