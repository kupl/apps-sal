N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if N > K:
    SUM = X*K + Y*(N - K)
else:
    SUM = X*N
print(SUM)

