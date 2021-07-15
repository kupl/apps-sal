import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    n,k=list(map(int,input().split()))
    A=list(map(int,input().split()))
    W=list(map(int,input().split()))

    W.sort()
    A.sort(reverse=True)

    ANS=[[] for i in range(k)]

    ind=0
    for i in range(k):
        ANS[i].append(A[ind])
        ind+=1
        W[i]-=1

    for i in range(k):
        while W[i]:
            ANS[i].append(A[ind])
            ind+=1
            W[i]-=1

    L=0
    for ans in ANS:
        L+=max(ans)+min(ans)
    print(L)

    

