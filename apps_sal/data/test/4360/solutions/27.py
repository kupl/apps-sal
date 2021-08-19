import numpy as np
n = int(input())
l = [np.array(input().split(), dtype=np.int64)]
l2 = []
for i in range(len(l)):
    l2.append(1 / l[i])
    sum1 = np.sum(l2)
    ans = 1 / sum1
print(ans)
