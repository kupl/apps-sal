n = int(input())

arr = list(map(int, input().split()))
print(len(set(arr)) - (int(0 in arr)))
