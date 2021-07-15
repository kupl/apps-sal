def calc_pow(x, y):
    if y == 0:
        return 1

    else:
        ans = calc_pow(x, y//2)**2

        if y%2:
            ans *= x
        
        return ans % 1000000007

def calc_X(c):
    X = 1
    k = n
    for i in range(c):
        X = (X * k) % 1000000007
        k = k-1

    return X

def calc_Y(c):
    Y = 1
    for i in range(1, c+1):
        Y = (Y * i) % 1000000007

    return Y

n, a, b = list(map(int, input().split()))

ans = calc_pow(2, n) - 1

XYa = (calc_X(a) * calc_pow(calc_Y(a), 1000000005)) % 1000000007
XYb = (calc_X(b) * calc_pow(calc_Y(b), 1000000005)) % 1000000007

ans = (ans - XYa - XYb) % 1000000007
print(ans)

