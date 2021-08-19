(K, X) = map(int, input().split())
result = []
for i in range(1, K):
    result.append(X + i)
    result.append(X - i)
result.append(X)
result.sort()
b = []
for n in result:
    num = str(n)
    b.append(num)
print(' '.join(b))
