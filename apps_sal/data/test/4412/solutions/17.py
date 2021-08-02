import sys
q = int(input())
lines = sys.stdin.readlines()
res = []


def getMax(numset):
    n = max(numset)
    numset = set([j for j in numset if n % j != 0])
    return (n, numset)


for i in range(q):
    n = int(lines[2 * i])
    m = []
    numset = set()
    for j in lines[2 * i + 1].split():
        numset.add(int(j))
    total = max(numset)
    n = total
    if n // 2 in numset and n // 3 in numset and n // 5 in numset:
        total = n // 2 + n // 3 + n // 5
    for _ in range(3):
        if len(numset) == 0:
            break
        n, numset = getMax(numset)
        m.append(n)
        if sum(m) > total:
            total = sum(m)
    res.append(str(total))
print('\n'.join(res))
