(n, k) = map(int, input().split())
s = input().strip()
if n - k > k - 1:
    for i in range(k - 1):
        print('LEFT')
    for i in range(n):
        print('PRINT', s[i])
        if i < n - 1:
            print('RIGHT')
else:
    for i in range(n - k):
        print('RIGHT')
    for i in range(n):
        print('PRINT', s[n - i - 1])
        if i < n - 1:
            print('LEFT')
