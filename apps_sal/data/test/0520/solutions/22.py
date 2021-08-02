n = int(input())
arr = [int(s) for s in input().split()]
arr.sort()
print(arr[n // 2])
