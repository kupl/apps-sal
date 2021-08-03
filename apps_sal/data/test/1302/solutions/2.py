n, k = map(int, input().split())
if n - k == 0:
    print(-1)
elif n - k == 1:
    for i in range(n):
        print(i + 1, end=' ')
else:
    print(n, end=' ')
    for i in range(k):
        print(i + 2, end=' ')
    print(1, end=' ')
    for i in range(n - k - 2):
        print(k + i + 2, end=' ')
