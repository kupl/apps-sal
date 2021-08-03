n = int(input())
arr = list(map(int, input().strip().split()))

print(2 + (min(arr) ^ arr[2]))
