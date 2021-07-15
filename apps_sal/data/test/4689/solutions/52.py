K,N = map(int,input().split())
A1 = list(map(int,input().split()))

D = [0] * (N)

A2 = [A1[i]+K for i in range(len(A1)-1)]
A1 = A1+A2

for i in range(N):
    D[i] = A1[i+N-1] - A1[i]
    #print(A1[i],A1[i+N-1])
print(min(D))
