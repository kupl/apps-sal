(K, X) = map(int, input().split())
if K == 1:
    print(X)
elif K > 1:
    print(*range(X - K + 1, X + K))
