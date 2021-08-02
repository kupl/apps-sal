n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
print(arr[(n - 1) // 2])
