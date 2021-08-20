t = int(input())
for _ in range(t):
    (n, m, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        if arr[i] < max(arr[i + 1] - k, 0):
            if m < max(arr[i + 1] - k, 0) - arr[i]:
                print('NO')
                break
            else:
                m -= max(arr[i + 1] - k, 0) - arr[i]
        else:
            m += arr[i] - max(arr[i + 1] - k, 0)
    else:
        print('YES')
