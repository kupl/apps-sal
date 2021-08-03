n, a, b = tuple(map(int, input().split()))
nr1 = list(map(int, input().split()))
nr2 = list(map(int, input().split()))
for i in range(1, n + 1):
    if i in nr1:
        print('1', end=' ')
    else:
        print('2', end=' ')
