def solve(arr, n, k):
    s = 0
    for i in reversed(list(range(n))):
        for j in reversed(list(range(k))):
            if arr[i][j] == 0:
                m = min(arr[i + 1][j], arr[i][j + 1])
                if m == 1:
                    return -1
                arr[i][j] = m - 1
            s += arr[i][j]
            if j > 0 and arr[i][j - 1] >= arr[i][j]:
                return -1
            if i > 0 and arr[i - 1][j] >= arr[i][j]:
                return -1
    return s


(n, k) = [int(x) for x in input().split()]
arr = []
for _ in range(n):
    arr.append([int(x) for x in input().split()])
res = solve(arr, n, k)
print(res)
