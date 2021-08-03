t = int(input())
for i in range(t):
    n = int(input())
    arr = ''
    if (n % 2 == 1):
        arr = '7'
        for j in range((n - 3) // 2):
            arr += '1'
    else:
        for j in range(n // 2):
            arr += '1'
    print(arr)
