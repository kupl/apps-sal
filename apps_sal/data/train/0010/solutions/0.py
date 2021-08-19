for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [arr[0]]
    for i in range(1, n - 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            ans.append(arr[i])
        elif arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
            ans.append(arr[i])
    ans.append(arr[-1])
    print(len(ans))
    print(*ans)
