N=list(map(int,input().split()))
A=N[0]
B=N[1]
C=N[2]
D=N[3]
print(max(A*C,A*D,B*C,B*D))
