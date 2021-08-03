import collections
w = list(input())
wc = collections.Counter(w)
num = 0
for i, x in enumerate(wc):
    if(wc[x] % 2 == 0):
        num += 1
if(num == len(wc)):
    print('Yes')
else:
    print('No')
