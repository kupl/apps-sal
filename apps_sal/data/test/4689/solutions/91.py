import numpy as np

k, n = map(int, input().split())
a = list(map(int, input().split()))

dif = []
for i in range(len(a)):
    if i == 0:
        dif.append(k-a[-1]+a[0])
    else:
        dif.append(a[i]-a[i-1])

dif = np.array(dif)
max_dif_idx = np.argmax(dif)
print(dif.sum() - dif[max_dif_idx])
