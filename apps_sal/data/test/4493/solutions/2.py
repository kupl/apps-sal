import numpy as np
C = np.array([[int(x) for x in input().split()] for _ in range(3)])
ans = 'Yes'
for i in range(2):
    if not(C[0,i+1]-C[0,i] == C[1,i+1]-C[1,i] == C[2,i+1]-C[2,i]):
        ans = 'No'
    if not(C[i+1,0]-C[i,0] == C[i+1,1]-C[i,1] == C[i+1,2]-C[i,2]):
        ans = 'No'
print(ans)

