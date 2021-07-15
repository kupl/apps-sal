K, N = list(map(int, input().split()))
A = list(map(int, input().split()))



A = sorted(A)
L = []
ANS = 0

A_max = max(A)

for i in range(N-1):
    L.append(abs(A[i+1]-A[i]))
        
L.append(K + A[0] - A_max)

L = sorted(L)


L.pop(-1)

for i in range(len(L)):
    ANS = ANS + L[i]
    
print(ANS)

