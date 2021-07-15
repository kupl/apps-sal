import numpy as np

N = int(input())

LS = np.array([sum([1 for i in range((N - 1)//(j + 1))]) for j in range(N)])

print((sum(LS)))

