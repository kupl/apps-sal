n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = []
sumx = 0
for i in range(n):
    sumx += arr1[i]
    arr2.append(sumx)
j = 0
k = 0
while(j < m):
    if(arr[j] <= arr2[k]):
        if(k == 0):
            print(k + 1, arr[j])
        else:
            print(k + 1, arr[j] - arr2[k - 1])
    else:
        while(arr[j] > arr2[k]):
            k += 1
        print(k + 1, arr[j] - arr2[k - 1])
    j += 1
