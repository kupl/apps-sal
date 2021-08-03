from collections import defaultdict
n, s = [int(s) for s in input().split()]
buyq = defaultdict(int)
selq = defaultdict(int)
sq = 0
bq = 0
for i in range(n):
    d, p, q = input().split()
    p = int(p)
    q = int(q)
    if d == 'B':
        buyq[p] += q
    else:
        selq[p] += q
a = sorted(selq.keys())
for i in a[min(s, len(selq)) - 1::-1]:
    print("S", i, selq[i])

b = sorted(buyq.keys())
for i in b[::-1][:min(s, len(buyq)):]:
    print("B", i, buyq[i])
