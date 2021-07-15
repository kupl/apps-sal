import numpy as np
h,w = map(int,input().split())
s = [[] for j in range(h)]
for i in range(h):
    tmp = input()
    for j in tmp:
        if j == '.':
            s[i].append(1)
        else:
            s[i].append(0)


L = np.zeros((h,w))
R = np.zeros((h,w))
U = np.zeros((h,w))
D = np.zeros((h,w))
s = np.array(s)

for i in range(w):
    L[:,i] = (L[:,i-1]+1)*s[:,i]
    R[:,-1-i] = (R[:,-i]+1)*s[:,-1-i]
    
for i in range(h):
    U[i,:] = (U[i-1,:]+1)*s[i,:]
    D[-1-i,:] = (D[-i,:]+1)*s[-i-1,:]
    
print(int(np.max(L+R+D+U-3)))
