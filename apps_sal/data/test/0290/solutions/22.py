while True:
    n = int(input())

    sqrt_n = int(n**0.5)

    minn = 100000000

    if(sqrt_n*sqrt_n >= n):

        minn = min(minn, sqrt_n + sqrt_n)

    if(sqrt_n*(sqrt_n+1) >= n):

        minn = min(minn, sqrt_n + (sqrt_n+1))

    if((1+sqrt_n)*(1+sqrt_n) >= n):

        minn = min(minn, (1+sqrt_n) + (1+sqrt_n))

    print(minn)

    break

