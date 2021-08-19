(n, a, b) = [int(x) for x in input().split()]
arr = [[0] * b for i in range(a)]
cnt = 1
if n > a * b:
    print(-1)
else:
    flag = True
    for i in range(a):
        if flag:
            for j in range(b):
                if cnt <= n:
                    arr[i][j] = cnt
                    cnt += 1
            flag = False
        else:
            for j in range(b - 1, -1, -1):
                if cnt <= n:
                    arr[i][j] = cnt
                    cnt += 1
            flag = True
    for i in range(a):
        print(*arr[i])
