X, Y = map(int, input().split())

for i in range(X + 1):
    if 4 * i + 2 * (X - i) == Y:
        print('Yes')
        return
print('No')
