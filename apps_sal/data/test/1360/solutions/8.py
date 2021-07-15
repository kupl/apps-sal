n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = tuple(map(int, input().split()))
arr.sort()
end = arr[0][1]
for i in range(1, n):
    if end <= arr[i][1]:
        end = arr[i][1]
    else:
        end = arr[i][0]
print(end)
    

