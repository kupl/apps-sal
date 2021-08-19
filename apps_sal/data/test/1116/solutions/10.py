from math import gcd
for i in range(int(input())):
    r, b, k = map(int, input().split())
    if r > b:
        r, b = b, r
    t = r * b // (gcd(r, b))
    t -= 1
    m = (t // r) // (t // b + 1)
    if (t // r) % (t // b + 1):
        m += 1
    # print(m)
    if k <= m:
        print("REBEL")
    else:
        print("OBEY")
