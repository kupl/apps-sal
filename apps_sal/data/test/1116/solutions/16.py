from math import gcd

T = int(input())
for i in range(T):
    r, b, k = map(int, input().split())
    if r > b:
        tmp = r
        r = b
        b = tmp

    g = gcd(r, b)
    r = r // g
    b = b // g
    if r * (k - 1) + 1 < b:
        print("REBEL")
    else:
        print("OBEY")
