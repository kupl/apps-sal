N = int(input())
S = list(str(input()))
hyp = [["S", "S"], ["S", "W"], ["W", "S"], ["W", "W"]]
flag = 0
for i in range(4):
    if flag == 2:
        break
    flag = 0
    ans = []
    ans.append(hyp[i][0])
    ans.append(hyp[i][1])
    for j in range(1, N + 1):
        if j >= N - 1:
            if j == N:
                j = 0
                t = 1
            else:
                t = 0

            if ans[j] == "S":
                if S[j] == "o":
                    if ans[j - 1] == "S":
                        if ans[t] == "S":
                            flag += 1
                    else:
                        if ans[t] == "W":
                            flag += 1
                else:
                    if ans[j - 1] == "S":
                        if ans[t] == "W":
                            flag += 1
                    else:
                        if ans[t] == "S":
                            flag += 1
            else:
                if S[j] == "o":
                    if ans[j - 1] == "S":
                        if ans[t] == "W":
                            flag += 1
                    else:
                        if ans[t] == "S":
                            flag += 1
                else:
                    if ans[j - 1] == "S":
                        if ans[t] == "S":
                            flag += 1
                    else:
                        if ans[t] == "W":
                            flag += 1

        else:
            if ans[j] == "S":
                if S[j] == "o":
                    if ans[j - 1] == "S":
                        ans.append("S")
                    else:
                        ans.append("W")
                else:
                    if ans[j - 1] == "S":
                        ans.append("W")
                    else:
                        ans.append("S")
            else:
                if S[j] == "o":
                    if ans[j - 1] == "S":
                        ans.append("W")
                    else:
                        ans.append("S")
                else:
                    if ans[j - 1] == "S":
                        ans.append("S")
                    else:
                        ans.append("W")

if flag != 2:
    print(-1)
else:
    for i in range(len(ans)):
        if i != len(ans) - 1:
            print(ans[i], end="")
        else:
            print(ans[i])
