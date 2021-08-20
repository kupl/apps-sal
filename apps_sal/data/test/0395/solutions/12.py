arr = list(map(int, input().split()))
flag = 0
s = sum(arr)
for i in range(4):
    for j in range(i + 1, 5):
        for k in range(j + 1, 6):
            h = arr[i] + arr[j] + arr[k]
            if s - h == h:
                print('YES')
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        break
if flag == 0:
    print('NO')
