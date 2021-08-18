import numpy as np

x, y, a, b, c = [int(i) for i in input().split()]
p = np.array([int(i) for i in input().split()])
q = np.array([int(i) for i in input().split()])
r = np.array([int(i) for i in input().split()])

p.sort()
q.sort()
r.sort()

p = p[-x:]
q = q[-y:]
if x + y < r.size:
    r = r[-x - y:]
apple = np.hstack([p, q, r])
apple.sort()

sweet = apple[-x - y:].sum()

print(sweet)
