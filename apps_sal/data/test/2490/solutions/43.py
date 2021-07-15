n='0'+input()

X=[]
for i in range(len(n)):
    X.append(int(n[i]))
cnt=0
i=len(n)-1
while i>=0:
    if X[i]>5:
        cnt+=10-X[i]
        X[i-1]+=1
        
    elif X[i]==5:
        cnt+=5
        if X[i-1]>=5:
            X[i-1]+=1
    else:
        cnt+=X[i]
    i-=1
print(cnt)

