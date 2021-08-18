N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    daikin = X * N
else:
    daikin = X * K + Y * (N - K)
print(daikin)
