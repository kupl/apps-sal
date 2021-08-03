import itertools
from collections import Counter
n = int(input())
ln = len(str(n))

if ln == 10:
    ln = 9

res = 0

seq = ("3", "5", "7")

for i in range(3, ln + 1):
    temp = list(itertools.product(seq, repeat=i))
    for j in temp:
        ja = Counter(j)
        if ja["3"] * ja["5"] * ja["7"] > 0:
            jj = ''.join(j)
            tempp = int(jj)
            if tempp <= n:
                res += 1

print(res)
