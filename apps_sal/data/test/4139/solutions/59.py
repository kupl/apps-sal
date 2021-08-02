from itertools import product
from collections import Counter

N = input()
res = 0

S = []
for i in range(1, len(N) + 1):
    for num in product('357', repeat=i):
        S.append(''.join(num))
for s in S:
    if(len(Counter(s)) == 3 and int(s) <= int(N)):
        res += 1
print(res)
