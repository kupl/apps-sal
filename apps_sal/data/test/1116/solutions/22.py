import math


def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


t = int(input())
for __ in range(t):
    r, b, k = list(map(int, input().split()))
    gcd_rb = gcd(r, b)
    r_n = r // gcd_rb
    b_n = b // gcd_rb
    if r_n < b_n:
        r_n, b_n = b_n, r_n
    streak = math.ceil((r_n - 1) / b_n)
    if streak < k:
        print("OBEY")
    else:
        print("REBEL")
