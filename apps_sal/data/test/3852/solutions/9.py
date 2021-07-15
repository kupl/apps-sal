n=int(input())
A=[int(i) for i in input().split()]

mode=0
cnt=0

ans=[]

def do(a,b):
    nonlocal cnt
    cnt+=1
    A[b]+=A[a]
    ans.append((a+1,b+1))

def doMAX(b):
    if b==-1:
        b+=n
    do(A.index(max(A)),b)

def doMIN(b):
    if b==-1:
        b+=n
    do(A.index(min(A)),b)

if abs(max(A))>=abs(min(A)):
    doMAX(-1)
    mode=0
elif abs(max(A))<abs(min(A)):
    doMIN(0)
    mode=1
else:
    doMAX(-1)
    mode=0

if mode==0:
    old=-10**30
    for i in range(n-1):
        if A[i]>=old:
            old=A[i]
            continue
        while A[i]+A[-1]<old:
            doMAX(-1)
        doMAX(i)
        old=A[i]
    while A[-1]<old:
        doMAX(-1)
    #print(A,cnt)
elif mode==1:
    old=10**30
    for i in range(n-1,0,-1):
        if A[i]<=old:
            old=A[i]
            continue
        while A[i]+A[0]>old:
            doMIN(0)
        doMIN(i)
        old=A[i]
    while A[0]>old:
        doMIN(0)
    #print(A,cnt)
else:
    pass
#print(A,cnt)
print(cnt)
for ele in ans:
    print((ele[0],ele[1]))

