
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if ((1 <= N & N <= 10000) & (1 <= K & K <= 10000)) \
        & (1 <= X & X <= 10000) & (1 <= Y & Y <= 10000):
    if (X > Y):
        price = 0
        if (N < K):
            for i in range(1, N + 1):
                price += X
        if (N >= K):
            for i in range(1, K + 1):
                price += X
            for j in range(K + 1, N + 1):
                price += Y
        print(price)
