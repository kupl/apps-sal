import math
(n, m) = map(int, input().split(' '))
pyL = sorted([[i] + list(map(int, input().split(' '))) for i in range(m)], key=lambda x: x[2])
li = [1] * (n + 1)
for i in range(len(pyL)):
    (index, p, y) = pyL[i]
    pyL[i].append(str(p).zfill(6) + str(li[p]).zfill(6))
    li[p] += 1
for py in sorted(pyL, key=lambda x: x[0]):
    print(py[3])
