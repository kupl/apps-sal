import numpy as np

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
s_np = np.array(s)


if min(s_np[:, 1]) - max(s_np[:, 0]) >= 0:
    print(min(s_np[:, 1]) - max(s_np[:, 0]) + 1)
else:
    print(0)
