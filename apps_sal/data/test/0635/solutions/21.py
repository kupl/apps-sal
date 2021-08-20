(s, n) = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
flag = 0
if arr1[0] == 0:
    flag = 1
elif arr1[n - 1] == 0 and arr2[n - 1] == 0:
    flag = 1
elif arr1[n - 1] == 0:
    temp = 0
    for j in range(n, s):
        if arr1[j] == 1 and arr2[j] == 1:
            temp = 1
            break
    if temp == 0:
        flag = 1
if flag == 0:
    print('YES')
else:
    print('NO')
