import math
from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
B = list(map(int, input().split()))
C = Counter(B)
CKEY = sorted(list(C.keys()), reverse=True)
x = 2750131
L = math.floor(math.sqrt(x))
Primelist = [i for i in range(x + 1)]
Primelist[1] = 0
for i in Primelist:
    if i > L:
        break
    if i == 0:
        continue
    for j in range(2 * i, x + 1, i):
        Primelist[j] = 0
Primes = [Primelist[j] for j in range(x + 1) if Primelist[j] != 0]
DICT = {Primes[i]: i + 1 for i in range(199999)}
ANS = []
for k in CKEY:
    while C[k] > 0:
        if k in DICT:
            x = DICT[k]
            ANS.append(x)
            C[k] -= 1
            C[x] -= 1
        else:
            for p in Primes:
                if k % p == 0:
                    C[k] -= 1
                    C[k // p] -= 1
                    ANS.append(k)
                    break
print(*ANS)
