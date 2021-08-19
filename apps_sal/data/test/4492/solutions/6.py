(N, X) = (int(T) for T in input().split())
A = [int(T) for T in input().split()]
Eat = 0
for AN in range(0, N - 1):
    if A[AN] + A[AN + 1] > X:
        Need = A[AN] + A[AN + 1] - X
        if A[AN + 1] >= Need:
            A[AN + 1] -= Need
        else:
            A[AN] -= Need - A[AN + 1]
            A[AN + 1] = 0
        Eat += Need
print(Eat)
