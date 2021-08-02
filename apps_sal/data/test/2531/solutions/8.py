def bin_search(A, val):
    l = 0; flag = 0
    r = len(arr) - 1
    while l < r:
        #print(l, r)
        if ((A[l] + A[r]) == 2 * val):
            flag += 1
            break
        elif (A[l] + A[r] < 2 * val):
            l += 1
        elif(A[l] + A[r] > 2 * val):
            r -= 1
    return flag


n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

cnt = 0
arr.sort()
# print(arr)
for i in range(n):
    x = bin_search(arr, arr[i])
    if(x == 1):
        cnt += 1
print(cnt)
