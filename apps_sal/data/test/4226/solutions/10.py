(x, y) = map(int, input().split())
for i in range(x + 1):
    if 2 * (x - i) + 4 * i == y:
        print('Yes')
        break
else:
    print('No')
