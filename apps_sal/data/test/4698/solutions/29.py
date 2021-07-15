N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = []
X = []
for i in range(M):
    p, x = list(map(int, input().split()))
    P.append(p)
    X.append(x)

Sum = sum(T)
for i in range(M):
    print((Sum - T[P[i] - 1] + X[i]))

