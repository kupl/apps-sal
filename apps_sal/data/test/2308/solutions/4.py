for _ in range(int(input())):
    x = input()
    y = input()
    sh = len(y) - y.rfind("1")
    cnt = 0
    for i in range(len(x) - sh, -1, -1):
        if x[i] == "1":
            break
        else:
            cnt += 1
    print(cnt)
