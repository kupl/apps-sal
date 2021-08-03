from math import gcd

N = int(input())

all_t = []
gcd_all = 0

if N >= 2:
    for i in range(N):
        all_t.append(int(input()))

        if i == 1:
            gcd_all = gcd(all_t[0], all_t[1])
            base = int(all_t[0] * all_t[1] // gcd_all)
        elif i >= 2:
            gcd_all = gcd(base, all_t[i])
            base = int(base * all_t[i] // gcd_all)
    print(base)
else:
    print((int(input())))
