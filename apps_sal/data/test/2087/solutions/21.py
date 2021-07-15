A=list(map(lambda X:X*(X+1)//2, map(int,input().split())))
print(A[0]*A[1]*A[2]%998244353)
