from collections import Counter
import math
N = int(input())
Nso = []
Nruto = math.sqrt(N)
Nruto = math.floor(Nruto)
for i in range(2, Nruto + 1):
    while N % i == 0:
        N = N // i
        Nso.append(i)
    if N == 1:
        break
    Nruto = math.sqrt(N)
    Nruto = math.floor(Nruto)
Nso.append(N)
if 1 in Nso:
    Nso.remove(1)
Nso = Counter(Nso)
ans = 0
for v in list(Nso.values()):
    count = 0
    for i in range(1, v + 1):
        if count + i > v:
            break
        else:
            count += i
            ans += 1
print(ans)
