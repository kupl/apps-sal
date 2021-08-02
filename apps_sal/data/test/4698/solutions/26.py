N = int(input())
T = list(map(int, input().split()))
M = int(input())
for i in range(M):
    P, X = list(map(int, input().split()))
    Y = T[P - 1]
    T[P - 1] = X
    print((sum(T)))
    T[P - 1] = Y
