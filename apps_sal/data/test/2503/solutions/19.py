import numpy as np
N, K = list(map(int, input().split()))
ub = K * 2
b = [[0 for j in range(ub + 1)] for i in range(ub + 1)]
ADD = {"B": 0, "W": K}

def create_bound(p, K, ub):
	if p - K + 1 >= 0:
		return [(p - K + 1, p + 1)]
	else:
		return [(0, p + 1), ((p - K + 1) % ub, ub)]

for i in range(N):
	x, y, c = input().split()
	nx = int(x) % ub
	ny = (int(y) + ADD[c]) % ub
	for add in [0, K]:
		for xlb, xub in create_bound((nx + add) % ub, K, ub):
			for ylb, yub in create_bound((ny + add) % ub, K, ub):
				b[xlb][ylb] += 1
				b[xlb][yub] -= 1
				b[xub][ylb] -= 1
				b[xub][yub] += 1

b_arr = np.array(b)
for i in range(ub):
	b_arr[i + 1, :] += b_arr[i, :]
for j in range(ub):
	b_arr[:, j + 1] += b_arr[:, j]
print((b_arr.max()))

