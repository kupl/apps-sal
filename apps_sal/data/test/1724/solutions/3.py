import sys
N=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))
Sums=[0]*(N)
m=sys.stdin.readline()


maxx=0
s=0
for i in range(N):
    s+=A[i]
    Sums[i]=s
    if(m[i]=="1"):
        maxx+=A[i]
ind=N-1
for i in range(N):
    if(m[i]!="1"):
        ind=i
        break
temp_ans=0

conf=""
for i in range(N-1,0,-1):
    if(i==ind):
        break
    if(m[i]=="1"):
        temp_ans+=A[i]
        if(A[i]<Sums[i-1]):
            ans=temp_ans-A[i]+Sums[i-1]
            if(ans>maxx):
                maxx=ans
print(maxx)

