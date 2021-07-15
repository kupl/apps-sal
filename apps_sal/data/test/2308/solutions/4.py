for _ in range(int(input())):
    x = input()
    y = input()
    sh = len(y) - y.rfind("1")
    #ans = 0
    cnt = 0
    for i in range(len(x) - sh, -1, -1):
        if x[i] == "1":
            #ans = cnt 
            break
        else:
            cnt += 1
    print(cnt)

