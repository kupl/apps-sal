n, k = list(map(int, input().split()))
p = list(map(int, input().split()))

arr = [[] for i in range(256)]
ans = []
for i in p:
    j = i
    if len(arr[i]) == 0:
        c = 0
        while c < k and j >= 0:
            if len(arr[j]) + c > k:
                break
            # temp=len(arr[j])
            if len(arr[j]) != 0:
                arr[i].extend(arr[j])
                break
            arr[j] = arr[i]
            arr[j].append(j)
            j -= 1
            c += 1
        arr[i].sort()
    ans.append(arr[i][0])
print(*ans)
# print(arr)
