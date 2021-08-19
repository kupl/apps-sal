import numpy as np
N = int(input())
As = np.array(list(map(int, input().split())), dtype='int64')
minus_num = len(np.where(As < 0)[0])
abs_As = np.abs(As)
if 0 in As or minus_num % 2 == 0:
    print(sum(abs_As))
else:
    print(sum(abs_As) - 2 * min(abs_As))
