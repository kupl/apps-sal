import numpy as np
N,M,C=map(int,input().split())
B=np.array(list(map(int,input().split())))
ans = 0
for _ in range(N):
    A = np.array(list(map(int,input().split())))
    if np.sum(A*B)+C > 0:
        ans += 1
print(ans)
