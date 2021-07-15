N,X = (int(T) for T in input().split())
A = [int(T) for T in input().split()]
Eat = 0
for AT in range(0,N-1):
    if A[AT]+A[AT+1]>X:
        Need = A[AT]+A[AT+1]-X
        Eat += Need
        A[AT] -= max(0,Need-A[AT+1])
        A[AT+1] = max(0,A[AT+1]-Need)
print(Eat)
