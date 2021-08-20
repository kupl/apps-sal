n = int(input())
arr = list(map(int, input().strip().split()))
arr = sorted(arr, reverse=True)
ans = [0] * n
if n == 2:
    print(*arr)
else:
    ans[0] = arr[0]
    ans[1] = arr[1]
    ans[n - 1] = arr[2]
    if n == 3:
        print(*ans)
    else:
        l = 1
        h = n - 1
        for i in range(3, n):
            if arr[i] - ans[l] > arr[i] - ans[h]:
                ans[h - 1] = arr[i]
                h -= 1
            else:
                ans[l + 1] = arr[i]
                l += 1
        print(*ans)
