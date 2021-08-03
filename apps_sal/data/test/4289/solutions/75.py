import numpy as np
N = int(input())
T, A = (int(x) for x in input().split())

result = [int(N) for N in input().split()]

list = []
for num in range(N):
    list.append(abs(T - 0.006 * result[num] - A))

m = np.argmin(list) + 1

print(m)
