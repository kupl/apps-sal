arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    x = int(input())
    if x in arr1:
        arr1[arr1.index(x)] -= x
    elif x in arr2:
        arr2[arr2.index(x)] -= x
    elif x in arr3:
        arr3[arr3.index(x)] -= x
    if _ >= 3:
        if arr1[0] == arr1[1] and arr1[1] == arr1[2]:
            print("Yes")
            return
        if arr2[0] == arr2[1] and arr2[1] == arr2[2]:
            print("Yes")
            return
        if arr3[0] == arr3[1] and arr3[1] == arr3[2]:
            print("Yes")
            return
        for jj in range(3):
            if arr1[jj] == arr2[jj] and arr2[jj] == arr3[jj]:
                print("Yes")
                return
        if arr1[0] == arr2[1] and arr2[1] == arr3[2]:
            print("Yes")
            return
        if arr1[2] == arr2[1] and arr2[1] == arr3[0]:
            print("Yes")
            return
print("No")
