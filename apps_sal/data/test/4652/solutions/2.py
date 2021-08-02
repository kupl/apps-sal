q = int(input())
for i in range(q):
    n = int(input())
    arr = [int(x) for x in input().split()]
    l = arr[0]
    forwards = True
    back = True
    for j in range(n - 1):
        if arr[j] - 1 != (arr[0] - 1 + j) % n:
            forwards = False
        if arr[j] - 1 != (arr[0] - 1 - j) % n:
            back = False
    if forwards == True or back == True:
        print("YES")
    else:
        print("NO")
