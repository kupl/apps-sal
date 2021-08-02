n, k = map(int, input().split())
for i in range(1, n + 1):
    if(k > 0):
        print(2 * i - 1, end=' ')
        print(2 * i, end=' ')
        k -= 1
    else:
        print(2 * i, end=' ')
        print(2 * i - 1, end=' ')
        k -= 1
