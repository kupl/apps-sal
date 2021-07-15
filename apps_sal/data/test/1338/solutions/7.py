__author__ = 'yushchenko'

def countf(f):
    sum = 0
    for i in range(len(f)):
        for j in range(len(f))[i:]:
            # print(i, j)
            # print(f[i:j + 1])
            sum += min(f[i:j + 1])
    return sum

import itertools
n,m = input().split()
n = int(n)
m = int(m)
maxf = 0;
count = 0;
save = ()
for x in itertools.permutations(list(range(n + 1))[1:]):
    t = countf(x)
    if t > maxf:
        maxf = t
        count = 0
    if t == maxf:
        # print (x , '-' , t)
        count = count + 1
        if count == m:
            save = x
print(' '.join(str(e) for e in save))




