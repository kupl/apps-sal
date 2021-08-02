import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = []
for i in range(n):
    arr1.append(list(map(int, input().split())))

arr2 = []
for i in range(n):
    arr2.append(list(map(int, input().split())))

arr3 = []
arr4 = []
for i in range(n):
    arr3.append([])
    arr4.append([])
    for j in range(m):
        arr3[i].append(min(arr1[i][j], arr2[i][j]))
        arr4[i].append(max(arr1[i][j], arr2[i][j]))

flag = False
for i in range(n):
    for j in range(m):
        try:
            if arr3[i][j] >= arr3[i][j + 1] or arr4[i][j] >= arr4[i][j + 1]:
                print("Impossible")
                flag = True
                break
        except:
            pass

        try:
            if arr3[i][j] >= arr3[i + 1][j] or arr4[i][j] >= arr4[i + 1][j]:
                print("Impossible")
                flag = True
                break
        except:
            pass

    if flag:
        break

if not flag:
    print("Possible")
