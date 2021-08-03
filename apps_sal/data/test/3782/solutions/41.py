import bisect
n, k, q = map(int, input().split())
a = list(map(int, input().split()))
if q == 1:
    print(0)
    return()
ls = [-1, n]
b = sorted(((a[i], i) for i in range(n)))
ansls = [b[q - 1][0] - b[0][0]]
space = [n]
qc = q
for i, x in enumerate(b):
    for j in range(i, n):
        idx = bisect.bisect_left(ls, b[j][1])
        if space[idx - 1] < k:
            continue
        qc -= 1
        space[idx - 1] -= 1
        if qc == 0:
            ansls.append(b[j][0] - x[0])
            break
    ins = bisect.bisect_left(ls, x[1])
    ls.insert(ins, x[1])
    space = []
    qc = q
    for j in range(1, i + 3):
        space.append(ls[j] - ls[j - 1] - 1)
print(min(ansls))
