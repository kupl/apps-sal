for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        arr.append((a, b, c, d))
    if(m % 2 == 1):
        print("NO")
    else:
        b, x = 0, 1
        for i in range(n):
            if(arr[i][1] == arr[i][2]):
                b = 1
        if(b == 0):
            x = 0
        b = 0
        if(m >= 4):
            for i in range(n):
                for j in range(n):
                    if(arr[i][1] == arr[j][2] and arr[i][2] == arr[j][1] and arr[i][0] == arr[j][0] and arr[i][3] == arr[j][3]):
                        b = 1
            if(b == 0):
                x = 0
        if(x == 0):
            print("NO")
        else:
            print("YES")
