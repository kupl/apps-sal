import numpy as np
a = np.array(list(map(int, list(input()))), dtype=np.int64).sum() % 9 == 0
if a:
    print("Yes")
else:
    print("No")
