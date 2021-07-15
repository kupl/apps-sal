from collections import defaultdict as dd, deque
n = int(input())
A = [int(x) for x in input().split()]
cA = [0]
for a in A:
    cA.append(cA[-1] + a)

B = dd(list)

for l in range(1,n+1):
    for i in range(n-l+1):
        s = cA[i+l] - cA[i]
        B[s].append((i,i+l))

best = 0
bestb = None
for b in sorted(B, key=lambda b: len(B[b]), reverse=True):
    if best > len(B[b]):
        break
    A = sorted(B[b], key=lambda x: x[1])
    res = 0
    lr = -1
    for l,r in A:
        if lr <= l:
            lr = r
            res += 1

    if res > best:
        best = res
        bestb = b

print(best)
A = sorted(B[bestb], key=lambda x: x[1])
res = 0
lr = -1
for l,r in A:
    if lr <= l:
        lr = r
        res += 1
        print(l+1,r)

