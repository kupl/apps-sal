import numpy as np
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if np.linalg.norm(np.array(X[i])-np.array(X[j])).is_integer():
            cnt += 1
print(cnt)
