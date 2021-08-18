import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))

result = 1 / np.sum(1 / A)

print(result)
