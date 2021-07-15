__author__ = 'taras-sereda'

from collections import Counter

n,k = list(map(int,input().split()))
sequence = list(map(int,input().split()))
r = Counter(sequence)
l = dict.fromkeys(r,0)
# print(sequence)
# print(r)
res = 0
for i in sequence:
    r[i] -= 1
    if i%k == 0 and int(i*k) in r and int(i/k) in l:

        res += r[i*k] * l[i/k]
    l[i] += 1

print(res)



