N=int(input())
A=list(map(int,input().split()))
core=1
b=A[0]
for i in range(1,N):
    if b>A[i]:
        core+=1
        b=A[i]
    else:
        pass
print(core)
