def solve(arr, n):
    arr.sort()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] != arr[j] != arr[k] and arr[k] - arr[i] <= 2:
                    return True
    return False


n = int(input())
arr = list(map(int, input().split()))

if solve(arr, n):
    print("YES")
else:
    print("NO")
