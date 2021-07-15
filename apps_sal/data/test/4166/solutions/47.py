n,m=list(map(int,input().split()))
o=[list(map(int,input().split()))for i in range(m)]
for i in range(10**n):
    if len(str(i))==n and all(str(i)[j-1]==str(k) for j,k in o):
        print(i)
        break
else:print((-1))

