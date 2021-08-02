n = int(input())

arr = list(map(int, input().split()))

x, y = arr.index(max(arr)), arr.index(min(arr))

print(max(n - 1 - x, n - 1 - y, x, y))
