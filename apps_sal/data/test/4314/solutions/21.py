import numpy as np

h, w = list(map(int, input().split()))
a = np.array([list(input()) for _ in range(h)])

for i in range(h):
    if np.count_nonzero(a[i] == '#') == 0:
        a[i] = 'x'
for i in range(w):
    if np.count_nonzero(a[:, i] == '#') == 0:
        a[:, i] = 'x'

for i in range(h):
    if res := ''.join([x for x in a[i] if x != 'x']):
        print(res)

