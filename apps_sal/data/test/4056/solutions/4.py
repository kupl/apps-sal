from math import gcd
n = int(input())
(*l,) = map(int, input().split())
tmp = l[0]
for i in range(1, n):
    tmp = gcd(tmp, l[i])
if tmp != 1:
    c = 2
    for i in range(2, int(tmp ** 0.5 + 1)):
        if tmp % i == 0:
            c += 2
            if i * i == tmp:
                c -= 1
    print(c)
else:
    print(1)
