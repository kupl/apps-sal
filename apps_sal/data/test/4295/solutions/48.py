(N, K) = map(int, input().split())
modK = N % K
if modK <= K // 2:
    print(modK)
else:
    print(K - modK)
