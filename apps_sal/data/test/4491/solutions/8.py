import numpy as np
N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A1_sum = [np.sum(A1[:N - i]) for i in range(N)]
A2_sum = [np.sum(A2[N - 1 - i:]) for i in range(N)]
A_sum = [A1_sum[i] + A2_sum[i] for i in range(N)]
print(np.max(A_sum))
