import numpy as np

k, n = map(int, input().split())
a_array = list(map(int, input().split()))

a_array.append(k + a_array[0])

a_diff = np.diff(a_array)
ans = np.sum(a_diff) - np.max(a_diff)
print(ans)
