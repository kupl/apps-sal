import numpy as np
(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = np.sort(a)
a = np.append(a, n + a[0])
a1 = np.append(0, a[:-1])
b = a - a1
b = b[1:]
print(np.sum(b) - np.max(b))
