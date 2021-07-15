import numpy as np

H, W = map(int, input().split())
S_list = [list(input()) for _ in range(H)]
S_list=(np.array(S_list) ==".")*1

L = np.zeros((H, W), int)
R = np.zeros((H, W), int)
U = np.zeros((H, W), int)
D = np.zeros((H, W), int)

for w in range(W):
    if w == 0:
        L[:,w] = S_list[:,w]
        R[:,W-w-1] = S_list[:,W-w-1]
    else:
        L[:,w] = (L[:,w-1]+1) * S_list[:,w]
        R[:,W-w-1] = (R[:,W-w]+1) * S_list[:,W-w-1]

for h in range(H):
    if h == 0:
        U[h,:] = S_list[h,:]
        D[H-h-1,:] = S_list[H-h-1,:]
    else:
        U[h,:] = (U[h-1,:]+1) * S_list[h,:]
        D[H-h-1,:] = (D[H-h,:]+1) * S_list[H-h-1,:]
        
ans = max(np.max(L+R+U+D-3), 0)

print(ans)
