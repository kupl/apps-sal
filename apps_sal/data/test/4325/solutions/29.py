(N, X, T) = map(int, input().split())
R = 0
RT = 0
while R < N:
    R += X
    RT += T
print(RT)
