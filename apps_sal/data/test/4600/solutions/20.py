import numpy as np
(n, m) = map(int, input().split())
a = np.array([list(input().split()) for i in range(m)])
b = [0] * (n + 1)
e = [0] * (n + 1)
c = 0
d = 0
for i in a:
    if b[int(i[0])] == 0:
        if i[1] == 'AC':
            c += 1
            b[int(i[0])] = 1
            d += e[int(i[0])]
        else:
            e[int(i[0])] += 1
print(c, d)
