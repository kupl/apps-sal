import numpy as np

N = int(input())
data_list = []
for i in range(N):
    si = input()
    data_list.append(si)

data_list = np.array(data_list)
print((len(np.unique(data_list))))
