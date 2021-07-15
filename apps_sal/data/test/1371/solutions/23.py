def calculate(n):
    arr = [0 for i in range(2000 + 1)]
    arr[3] = 1
    arr[4] = 1
    arr[5] = 1

    for i in range(6, n + 1):
        arr[i] = (arr[i - 2] + arr[i - 3] + arr[i - 4]) % (1000000000 + 7)
    print(arr[n])


calculate(int(input()))
