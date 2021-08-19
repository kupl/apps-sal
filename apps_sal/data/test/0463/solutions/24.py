from sys import stdin, stdout
(n, x) = stdin.readline().split()
(n, x) = (int(n), int(x))
arr = [int(y) for y in stdin.readline().split()]
arr.sort()
flag = 0
for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        print(0)
        flag = 1
        break
if flag == 0:
    arr1 = [arr[i] & x for i in range(len(arr))]
    arr2 = [(arr1[i], arr[i]) for i in range(len(arr))]
    arr2 = sorted(arr2, key=lambda x: x[0])
    currentAns = -1
    for i in range(len(arr2) - 1):
        if arr2[i][0] == arr2[i + 1][0]:
            if arr2[i][0] == arr2[i][1] or arr2[i + 1][0] == arr2[i + 1][1]:
                currentAns = 1
                flag = 1
                break
            else:
                currentAns = 2
    print(currentAns)
