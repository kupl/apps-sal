for _ in range(int(input())):
    n = int(input())
    i = 1
    j = 1
    cnt = 0
    while True:
        if n - int(str(i) * j) >= 0:
            cnt += 1
        else:
            break
        i += 1
        if i == 10:
            i = 1
            j += 1
    print(cnt)
