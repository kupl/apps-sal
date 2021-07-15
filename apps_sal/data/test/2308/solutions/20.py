t = int(input())
for i in range(t):
    x = input()
    y = input()
    num = y.rfind("1")
    if num != -1:
        if x.rfind("1") == -1:
            print(0)
        else:
            ans = 0
            for i in range(len(x) - len(y) + num,-1,-1):
                if x[i] == "1":
                    ans = len(x) - len(y) + num - i
                    break
            print(ans)
    else:
        print(0)
        

