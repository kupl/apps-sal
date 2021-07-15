n = int(input())
s = input()
a = ["SS", "SW", "WS", "WW"]
for i in a:
    ans = i
    for j in range(n - 2):
        if ans[j + 1] == "S":
            if s[j + 1] == "o":
                if ans[j] == "S":
                    ans += "S"
                else:
                    ans += "W"
            else:
                if ans[j] == "S":
                    ans += "W"
                else:
                    ans += "S"
        else:
            if s[j + 1] == "o":
                if ans[j] == "S":
                    ans += "W"
                else:
                    ans += "S"
            else:
                if ans[j] == "S":
                    ans += "S"
                else:
                    ans += "W"
    flag = True
    if ans[n - 1] == "S":
        if s[n - 1] == "o":
            if ans[n - 2] != ans[0]:
                flag = False
        else:
            if ans[n - 2] == ans[0]:
                flag = False
    else:
        if s[n - 1] == "o":
            if ans[n - 2] == ans[0]:
                flag = False
        else:
            if ans[n - 2] != ans[0]:
                flag = False
    if ans[0] == "S":
        if s[0] == "o":
            if ans[n - 1] != ans[1]:
                flag = False
        else:
            if ans[n - 1] == ans[1]:
                flag = False
    else:
        if s[0] == "o":
            if ans[n - 1] == ans[1]:
                flag = False
        else:
            if ans[n - 1] != ans[1]:
                flag = False
    if flag == True:
        print(ans)
        break
    else:
        continue
else:
    print(-1)
