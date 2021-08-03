import numpy as np
n, m, q = [int(i) for i in input().split()]

trains = np.zeros([n + 1, n + 1], dtype=np.int32)

l, r = np.split(np.array([input().split() for _ in range(m)], dtype=np.int32), 2, 1)
p, q = np.split(np.array([input().split() for _ in range(q)], dtype=np.int32), 2, 1)


np.add.at(trains, (l, r), 1)
ans_arr = np.cumsum(np.cumsum(trains, axis=0), axis=1)

p -= 1
ans = ans_arr[q, q] - ans_arr[p, q] - ans_arr[q, p] + ans_arr[p, p]
print(('\n'.join(ans.astype(str).flatten())))
