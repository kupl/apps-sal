n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if arr.count(arr[0]) == 2 * n:
    print(-1)
else:
    print(*arr)
