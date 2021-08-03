import numpy as np
n, m = map(int, input().split())
aa = [list(input()) for i in range(n)]
bb = [list(input())for i in range(m)]
a = np.array(aa)
b = np.array(bb)
for i in range(n - m + 1):
    for j in range(n - m + 1):

        if (a[i:i + m, j:j + m] == b).all():
            print('Yes')
            return
print('No')
