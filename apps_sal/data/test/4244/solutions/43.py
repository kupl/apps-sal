import numpy as np

n = int(input())
x = list(map(int, input().split()))
p = round(np.mean(x))
cost = np.dot(np.array(x) - p, np.array(x) - p)
print(int(cost))
