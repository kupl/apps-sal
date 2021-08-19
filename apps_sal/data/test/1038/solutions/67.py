(A, B) = list(map(int, input().split()))


def xor_func(n):
    if n % 2 == 0:
        tmp = n // 2
        if tmp % 2 == 0:
            x = 0 ^ n
        else:
            x = 1 ^ n
    else:
        tmp = (n + 1) // 2
        if tmp % 2 == 0:
            x = 0
        else:
            x = 1
    return x


f1 = xor_func(A - 1)
f2 = xor_func(B)
ans = f1 ^ f2
print(ans)
