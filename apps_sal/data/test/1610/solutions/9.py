(a, b) = list(map(int, input().split()))
for i in list(range(b + 1, 0, -1)) + list(range(b + 2, a + 1)):
    print(i, end=' ')
