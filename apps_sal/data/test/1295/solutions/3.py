import sys
def r(): return sys.stdin.readline()


n, m = map(int, r().split())
nrr = [int(x) for x in r().split()]
mrr = [int(x) for x in r().split()]

lrr = []
rrr = []
pointer = 0
for x in mrr:
    while True:
        if(pointer == n):
            break
        if(nrr[pointer] <= x):
            rrr.append(x - nrr[pointer])
            pointer += 1
        else:
            break
for i in range(pointer, n):
    rrr.append(10**10)

pointer = n - 1
for i in range(m - 1, -1, -1):
    while True:
        if(pointer == -1):
            break
        if(mrr[i] <= nrr[pointer]):
            lrr.append(nrr[pointer] - mrr[i])
            pointer -= 1
        else:
            break
for i in range(pointer, -1, -1):
    lrr.append(10**10)
srr = [min(lrr[i], rrr[n - i - 1]) for i in range(n)]
print(max(srr))
