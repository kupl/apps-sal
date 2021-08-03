n, k = list(map(int, input().split()))
i = 1
while i < (n - k):
    print(i, end='')
    print(' ', end='')
    i += 1
i = n
while i > n - k - 1:
    print(i, end='')
    print(' ', end='')
    i -= 1
