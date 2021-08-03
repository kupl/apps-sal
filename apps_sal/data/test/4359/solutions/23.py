import math
import numpy as np

time_list = []
for i in range(5):
    time_list.append(int(input()))

r_list = []
for i in time_list:
    r_list.append((i - 1) % 10)

x = np.argmin(r_list)
for i in range(5):
    if i != x:
        time_list[i] = int(math.ceil(time_list[i] * 0.1) * 10)
print(sum(time_list))
