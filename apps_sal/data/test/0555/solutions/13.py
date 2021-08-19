x = input()
arr = list(map(int, list(x)))
flag = False
for i in range(len(arr)):
    if arr[i] >= 5:
        if arr[i] != 9 or flag:
            arr[i] = 9 - arr[i]
    flag = True
print(''.join(list(map(str, arr))))
