N,K=map(int,input().split())
S='1'+input()+'1'
A=[]
now='1'
C=0
for s in S:
    if s==now:
        C+=1
    else:
        A.append(C)
        now=s
        C=1
A.append(C)
A[0]-=1
A[-1]-=1
B=[sum(A[:2*K+1])]
i=0
j=2*(K+1)
while j<len(A):
    b=B[-1]+sum(A[j-1:j+1])-sum(A[i:i+2])
    B.append(b)
    i+=2
    j+=2
print(max(B))
