t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    bol = [True for i in range(n)]
    flag = True
    while(flag):
        flag = False
        for i in range(n - 1):
            if(arr[n - i - 1] < arr[n - i - 2] and bol[n - i - 1]):
                bol[n - i - 1] = False
                tmp = arr[n - i - 1]
                arr[n - i - 1] = arr[n - i - 2]
                arr[n - i - 2] = tmp
                flag = True
    for x in range(n):
        if(x > 0):
            print(" ", end="")
        print(arr[x], end="")
    print()
