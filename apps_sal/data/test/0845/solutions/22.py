N=input()
S=input()
K='qwertyuiopasdfghjkl;zxcvbnm,./'
D=''
for i in range (0, len(S)):
    if N[0]=='R':
        D+=K[(K.find(S[i]))-1]
    else:
        D+=K[(K.find(S[i]))+1]
print(D)    
