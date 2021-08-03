for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = 0
    i = 0
    while i < n:
        if arr[i] < 0:
            if pos >= abs(arr[i]):
                pos += arr[i]
                arr[i] = 0
            else:
                arr[i] += pos
                pos = 0
        else:
            pos += arr[i]
        i += 1
    print(pos)
