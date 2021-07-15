N, A, B = map(int,input().split())

n1 = N // (A + B)
n2 = N % (A + B)

if n2 > A:
    print(A*(n1+1))
else:
    print(A*n1 + n2)
