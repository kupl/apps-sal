n = int(input())
arr = [int(x) for x in input().split()]
print(n*max(arr)-sum(arr))
