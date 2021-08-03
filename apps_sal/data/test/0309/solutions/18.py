from math import log2
l, r = list(map(int, input().split()))
if(l == r):
    print('0')
else:
    print((1 << int(log2(l ^ r) + 1)) - 1)
