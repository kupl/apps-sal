import sys
n = int(input())
s = input()

for ans in [["S", "S"], ["S", "W"], ["W", "S"], ["W", "W"]]:
    for i in range(n - 1):
        if s[(i + 1)] == "o":
            if ans[i + 1] == "S":
                if ans[i] == "S":
                    ans.append("S")
                else:
                    ans.append("W")
            else:
                if ans[i] == "S":
                    ans.append("W")
                else:
                    ans.append("S")
        if s[(i + 1)] == "x":
            if ans[i + 1] == "S":
                if ans[i] == "S":
                    ans.append("W")
                else:
                    ans.append("S")
            else:
                if ans[i] == "S":
                    ans.append("S")
                else:
                    ans.append("W")

    if ans[0] == ans[-1]:
        ans.pop()
        flag = 0
        if s[0] == "o":
            if ans[0] == "S":
                if ans[-1] == ans[1]:
                    flag = 1
            else:
                if ans[-1] != ans[1]:
                    flag = 1
        else:
            if ans[0] == "W":
                if ans[-1] == ans[1]:
                    flag = 1
            else:
                if ans[-1] != ans[1]:
                    flag = 1
        if flag == 1:
            print(("".join(ans)))
            return
print((-1))
