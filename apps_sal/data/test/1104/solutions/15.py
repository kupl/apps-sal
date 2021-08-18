n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
trr = [0 for i in range(n)]
for j in range(4):
    trr[0] = j
    fl = True
    for i in range(n - 1):
        if arr[i] == brr[i]:
            if trr[i] != arr[i]:
                fl = False
                break
            trr[i + 1] = arr[i]
        else:
            if brr[i] == 3:
                fl = False
                break
            if brr[i] == 2:
                if arr[i] == 3:
                    if trr[i] == 2:
                        trr[i + 1] = 3
                    elif trr[i] == 3:
                        trr[i + 1] = 2
                    else:
                        fl = False
                        break
                else:
                    fl = False
                    break
            if brr[i] == 1:
                if arr[i] == 3:
                    if trr[i] == 1:
                        trr[i + 1] = 3
                    elif trr[i] == 3:
                        trr[i + 1] = 1
                    else:
                        fl = False
                        break
                else:
                    fl = False
                    break
            if brr[i] == 0:
                if arr[i] == 1:
                    if trr[i] == 0:
                        trr[i + 1] = 1
                    elif trr[i] == 1:
                        trr[i + 1] = 0
                    else:
                        fl = False
                        break
                elif arr[i] == 2:
                    if trr[i] == 2:
                        trr[i + 1] = 0
                    elif trr[i] == 0:
                        trr[i + 1] = 2
                    else:
                        fl = False
                        break
                else:
                    if trr[i] == 1:
                        trr[i + 1] = 2
                    elif trr[i] == 2:
                        trr[i + 1] = 1
                    elif trr[i] == 3:
                        trr[i + 1] = 0
                    else:
                        trr[i + 1] = 3

    if fl:
        print('YES')
        print(*trr)
        break
else:
    print('NO')
