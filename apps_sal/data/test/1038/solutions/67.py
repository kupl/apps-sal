A, B = list(map(int, input().split()))
# F(A,B) = F(0,A-1) ^ F(0,B)
# 任意の偶数について、n ^ (n+1) = 1
# ex. F(0,6) = 0^1^2^3^4^5^6 = (0^1)^(2^3)^(4^5)^6 = 1^1^1^6
# 1^1^1^...について、1が偶数個なら0, 奇数個なら1


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

