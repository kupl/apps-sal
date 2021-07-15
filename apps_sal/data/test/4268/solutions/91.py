N,D=map(int, input().split())
X=[]
for i in range(N):
    X.append(list(map(int, input().split())))
count=0
for i in range(N):
    for j in range(N):
        if i >= j: continue
        d=0
        for k in range(D):
            d+=pow(abs(X[i][k]-X[j][k]),2)
        d=float(pow(d, 0.5))
        if d.is_integer(): count+=1
print(count)
