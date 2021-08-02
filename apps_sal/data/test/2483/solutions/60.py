import numpy as np
N, C = (int(x) for x in input().split())
R = [[0] * 100000 for _ in range(C)]  # R[c][t]:時刻t+1にチャンネルc+1を録画するのに必要な録画機の個数
R = np.array(R)
for _ in range(N):
    s, t, c = map(int, input().split())
    R[c - 1, s - 1:t] = 1
ans = max(sum(R))
print(ans)
