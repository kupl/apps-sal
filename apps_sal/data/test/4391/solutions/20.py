arr = list(map(int, input().split()))
n = arr[0]
k = arr[1]
arr = list(map(int, input().split()))
arr2 = []
for i in range(k, n + 1):
    temp = sum(arr[0:i])
    temp3 = temp
    for j in range(i, n):
        temp2 = temp3 + arr[j] - arr[j - i]
        temp3 = temp2
        if(temp2 > temp):
            temp = temp2
    arr2.append(temp / i)

print(max(arr2))
