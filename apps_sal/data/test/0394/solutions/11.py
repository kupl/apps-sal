n = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
ansarr = []
for i in range(1, n + 1):
    valarr = []
    for j in range(1, i + 1):
        val = arr[j] - arr[j - 1]
        valarr.append(val)
        flag = 0
    # print(valarr)
    for j in range(i + 1, n + 1):
        if(arr[j] != valarr[(j - 1) % i] + arr[j - 1]):
            flag = 1
            break

    if(flag == 0):
        ansarr.append(i)
print(len(ansarr))
print(*ansarr)
