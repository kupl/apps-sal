N = int(input())
A = list(map(int, input().split()))

temp = 0
pans = 0
isp = True
for i in range(N):
    temp += A[i]
    if isp: 
        if temp <= 0:
            pans+=-temp+1
            temp=1
        elif A[i]==0:
            pans+=1
            temp+=1
    else:
        if temp>=0:
            pans+=temp+1
            temp=-1
        elif A[i]==0:
            pans+=1
            temp-=1
    isp = not isp
temp = 0
mans = 0
isp = False
for i in range(N):
    temp += A[i]
    if isp: 
        if temp <= 0:
            mans+=-temp+1
            temp=1
        elif A[i]==0:
            mans+=1
            temp+=1
    else:
        if temp>=0:
            mans+=temp+1
            temp=-1
        elif A[i]==0:
            mans+=1
            temp-=1
    isp = not isp

print(min(pans,mans))
