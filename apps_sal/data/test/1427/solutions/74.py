n = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7
# Aたちの最小公倍数をMとすれば
# 答えはsum_{i}M/A_{i} (mod 10**9 + 7)


def lcm(X, Y):
    x = X
    y = Y
    if y > x:
        x, y = y, x
    while x % y != 0:
        x, y = y, x % y
    return X * Y // y


# (A,B,C)の最小公倍数　=(A,B)の最小公倍数とCの最小公倍数を利用すれば簡単そう.
a = 1
c = 0
s = 0
for i in range(n):
    q = lcm(a, A[i])
    s *= q // a
    a = q
    s += q // A[i]
print((s % mod))
