t = int(input())
for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    for i in range(n - 1):
        if arr[i] + 1 == arr[i + 1]:
            print(2)
            break
    else:
        print(1)
