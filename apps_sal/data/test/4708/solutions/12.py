# 044_a
# A - 高橋君とホテルイージー

N = int(input())  # 連泊数
K = int(input())  # 料金変動泊数
X = int(input())  # 通常価格
Y = int(input())  # 変動価格

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
