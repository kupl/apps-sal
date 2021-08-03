import numpy as np
N_List = np.array(list(map(int, input().split())))
N_List_a = np.sort(N_List)
print(sum(N_List_a[1:] - N_List_a[:-1]))
