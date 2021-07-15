t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    tmp  =sum(arr2)
    if tmp==0 or tmp==n:
        if sorted(arr1) == arr1:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
