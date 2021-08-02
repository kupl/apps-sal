K, X = map(int, input().split())

# K, X = 100程度なので、端点を考慮しなくてよい
# X−K+1,X−K+2,...,X+K−1 の2K−1個を出力すればよい
print(' '.join(map(str, range(X - K + 1, X + K))))
