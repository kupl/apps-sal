(X, Y) = map(int, input().split())
for i in range(Y // 4 + 1):
    if i * 4 + (X - i) * 2 == Y:
        print('Yes')
        break
else:
    print('No')
