import numpy as np
input()
a = np.array(sorted(map(int, input().split())))
print(min((sum((a - i) ** 2) for i in range(min(a), max(a) + 1))))
