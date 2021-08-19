def lcm(a):
    from math import gcd
    x = a[0]
    for i in range(1, len(a)):
        x = x * a[i] // gcd(x, a[i])
    return x


(A, B, C, D) = map(int, input().split())
num = []
num.append(C)
num.append(D)
a = A - 1
x_B = B - B // C - B // D + B // lcm(num)
x_A = a - a // C - a // D + a // lcm(num)
ans = x_B - x_A
print(ans)
