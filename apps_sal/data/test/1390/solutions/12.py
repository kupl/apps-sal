n,m=list(map(int,input().split()))
A=[]
A = list(map(int, input().split()))
A.sort()
B=[]
for i in range(m-n+1):
    B.append(A[n-1+i]-A[i])
B.sort()
print(B[0])
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             

