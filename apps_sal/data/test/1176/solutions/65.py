import numpy as np

N = int(input())
A = list(map(int, input().split()))


B = np.array(A)


num_minus = len(B[B < 0])
abs_tot = sum(list(map(abs, A)))
if num_minus % 2 == 0:
    print(abs_tot)
else:
    n_0 = 10**9
    for i in A:
        a = abs(i)
        if a < n_0:
            n_0 = a
    print(abs_tot - (n_0 * 2))
