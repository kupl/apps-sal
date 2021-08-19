(X, Y) = map(int, input().split())
count = 0
for i in range(0, X + 1):
    if i * 2 + (X - i) * 4 == Y:
        count += 1
if count > 0:
    print('Yes')
else:
    print('No')
