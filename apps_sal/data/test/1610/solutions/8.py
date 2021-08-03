a, b = list(map(int, input().split()))
for i in range(b + 1, 0, -1):
    print(i, end=' ')
for i in range(b + 2, a + 1):
    print(i, end=' ')
