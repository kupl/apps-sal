N,A,B = list(map(int,input().split()))

M = N//(A+B)

L = N%(A+B)

if L > A:
    L = A
    
print((A*M + L))

