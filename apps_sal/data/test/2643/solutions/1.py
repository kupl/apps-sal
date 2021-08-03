import numpy as np

k, q = map(int, input().split())
d = np.array(list(map(int, input().split())))
n = [0] * q
x = n.copy()
m = n.copy()
for i in range(q):
    n[i], x[i], m[i] = map(int, input().split())

for i in range(q):
    d_ = d % m[i]
    j = np.sum(d_ * ((n[i] - 1) // k)) + np.sum(d_[:(n[i] - 1) % k])
    s = np.sum(np.sum(d_ == 0) * ((n[i] - 1) // k)) + np.sum(d_[:(n[i] - 1) % k] == 0)
    count = n[i] - 1 - (j + x[i] % m[i]) // m[i] - s
    print(count)
