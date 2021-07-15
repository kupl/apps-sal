from collections import deque
S=input()
H=deque()
N=len(S)
num=0
for i in range(N):
    if len(H)>0 and H[-1]==S[i]:
        num+=1
        H.pop()
    else:
        H.append(S[i])
    #print(H)
#print(num)
if num%2==1:
    print('Yes')
else:
    print('No')

