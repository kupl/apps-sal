A=list(map(int,input().split()))

B=list(map(int,input().split()))

C=list(map(int,input().split()))

y=(A[1]+A[2]+(C[0]+C[1]-(B[0]+B[2])))//2

x=y+B[0]+B[2]-(A[1]+A[2])

z=y+B[0]+B[2]-(C[0]+C[1])

A[0]=x
B[1]=y
C[2]=z

print(A[0],A[1],A[2])
print(B[0],B[1],B[2])
print(C[0],C[1],C[2])

