# author:  Taichicchi
# created: 19.09.2020 00:06:44

import sys

K = int(input())

a = 7 % K

for k in range(K + 2):
    if a == 0:
        print((k + 1))
        break
    a = (a * 10 + 7) % K
else:
    print((-1))

