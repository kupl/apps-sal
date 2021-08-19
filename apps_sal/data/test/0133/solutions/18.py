def pow(a, b):
    if b == 0:
        return 1
    retvalue = pow(a, b // 2)
    retvalue *= retvalue
    retvalue %= 1000000007
    if b % 2 == 1:
        retvalue *= a
        retvalue %= 1000000007
    return retvalue


(n, m) = list(map(int, input().split()))
print(pow((pow(2, m) - 1) % 1000000007, n))
