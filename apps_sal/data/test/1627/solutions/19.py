n = int(input())
arr = [int(x) for x in input().split()]
while True:
    suc = 0
    for i in range(1, n):
        if(arr[i - 1] > arr[i]):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            print(i, i + 1)
            suc = 1
    if(suc == 0):
        break
