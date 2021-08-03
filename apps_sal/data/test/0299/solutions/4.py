n = int(input())
a = input().split()
arr = [0, 0, 0]
e = ["back", "chest", "biceps"]

for i in range(1, n + 1):
    arr[i % 3] += int(a[i - 1])

print(e[arr.index(max(arr))])
