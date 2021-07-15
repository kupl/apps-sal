N,K=map(int,input().split())
S=input()
A=[]
now=S[0]
if now=='0':
    A.append(0)
C=1
for s in S[1:]:
    if s==now:
        C+=1
    else:
        A.append(C)
        now=s
        C=1
A.append(C)
if now=='0':
    A.append(0)
B=[sum(A[:2*K+1])]
i=0
while 2*(i+K+1)<len(A):
    b=B[i]-(A[2*i]+A[2*i+1])+(A[2*(i+K+1)]+A[2*(i+K)+1])
    B.append(b)
    i+=1
print(max(B))
