def fun(a, b):
    cnt = 0
    while(True):
        cnt += a // b
        tmp = a
        a = b
        b = tmp % b
        if b == 0:
            break
    return cnt


a, b = [int(c) for c in input().split()]
print(fun(a, b))
