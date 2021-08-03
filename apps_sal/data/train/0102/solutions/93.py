t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    i = 1
    tmp = 1
    while (int(str(tmp) * i) <= n):
        cnt += 1
        if (tmp == 9):
            i += 1
            tmp = 1
        else:
            tmp += 1
    print(cnt)
