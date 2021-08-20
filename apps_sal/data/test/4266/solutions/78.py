(K, X) = map(int, input().split())
print(*list((i for i in range(X - K + 1, X + K))))
