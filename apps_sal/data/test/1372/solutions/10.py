import numpy as np
H,N= map(int, input().split())
m = np.array([list(map(int, input().split())) for _ in range(N)])
max_a = np.max(m[:,0])
dp = np.zeros(H+max_a+1, dtype='i8')
for i in range(max_a+1, H+max_a+1):
    dp[i] = np.min(dp[i-m[:,0]] + m[:,1])
print(dp[H+max_a])
