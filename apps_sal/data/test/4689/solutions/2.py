import numpy as np
K, N = map(int, input().split())
A = np.array(list(map(int, input().split())))
diff = np.append(A[1:] - A[:-1], K + A[0] - A[-1])
print(np.delete(diff, np.argmax(diff)).sum())
