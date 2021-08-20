import numpy as np
N = int(input())
(T, A) = map(int, input().split())
H = list(map(int, input().split()))
H = np.array(H)
temp = T - H * 0.006
res = np.abs(temp - A)
print(np.argmin(res) + 1)
