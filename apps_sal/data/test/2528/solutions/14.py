def subarr(arr):
    ans = 0
    cur = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            ans = max(ans, cur)
            cur = 0
        else:
            cur += 1
    return max(ans, cur)


eval(input())
arr = list(map(int, input().split()))
print(subarr(arr))
