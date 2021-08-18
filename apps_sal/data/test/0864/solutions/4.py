from collections import defaultdict as dd, deque

n, m = list(map(int, input().split()))
A = [int(x) for x in input().split()]

C = dd(int)
for a in A:
    C[a] += 1

psize = 1
while True:
    packs = 0
    for c in C:
        packs += C[c] // psize
    if packs < n:
        break
    psize += 1
print(psize - 1)
