n = int(input())
arr = []
for i in range(n):
    (a, b) = map(int, input().split())
    arr.append([a, b])
k = int(input())
for i in range(n):
    l = arr[i][0]
    r = arr[i][1]
    if r >= k:
        ind = i
        break
print(n - ind)
