import numpy as np
N = int(input())
a = np.array(list(map(int, input().split())))
a = a // 400

over_3200 = a[np.where(a >= 8)]
num_3200 = len(over_3200)

a = a[np.where(a <= 7)]
a_list = np.unique(a)
len_a = len(a_list)

if len_a == 0:
    min = 1
    num_3200 -= 1
else:
    min = len_a

max = min + num_3200
print(min, max)
