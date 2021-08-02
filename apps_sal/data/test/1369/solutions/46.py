# 解法3(山登り法)

import numpy as np

N = int(input())
x = np.zeros([N, 2])
for i in range(N):
    x[i, :] = list(map(float, input().split()))


def norm(x, y): return np.sqrt(((x - y)**2).sum())


x0 = x.mean(0)
old = x0
rate = 0.06
decay = 0.999
epsilon = 1e-15

while 1:
    d = np.sqrt(((x - old)**2).sum(1))
    max_, argmax = d.max(), d.argmax()
    direction = x[argmax, :] - old
    new = old + direction * rate
    rate *= decay
    if norm(new, old) <= epsilon: break
    old = new

print(norm(direction, 0))
