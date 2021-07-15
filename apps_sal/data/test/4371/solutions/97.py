# author:  Taichicchi
# created: 10.10.2020 23:35:00

import sys

S = input()

m = 10000000

for i in range(3, len(S) + 1):
    m = min(m, abs(753 - int(S[i - 3:i])))

print(m)

