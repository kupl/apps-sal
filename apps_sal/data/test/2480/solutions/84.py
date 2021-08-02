from collections import defaultdict
import numpy as np
n, k = map(int, input().split())
a = [0] + list(np.cumsum(list(map(int, input().split()))))

dic = defaultdict(int)
c = 0
for i in range(len(a)):
    p = (a[i] - i) % k
    c += dic[p]
    dic[p] += 1
    if i >= k - 1:
        dic[(a[i - k + 1] - (i - k + 1)) % k] -= 1
print(c)
