N = int(input())
s = input()
ans1 = "SS"
ans2 = "WS"
ans3 = "WW"
ans4 = "SW"
ans = [ans1, ans2, ans3, ans4]
c = 0
for j in range(4):
    for k in range(1, N - 1):
        if s[k] == "o":
            if ans[j][k] == "S":
                ans[j] += ans[j][-2]
            else:
                if ans[j][-2] == "W":
                    ans[j] += "S"
                else:
                    ans[j] += "W"
        if s[k] == "x":
            if ans[j][k] == "W":
                ans[j] += ans[j][-2]
            else:
                if ans[j][-2] == "W":
                    ans[j] += "S"
                else:
                    ans[j] += "W"
    if s[0] == "o":
        if ans[j][0] == "S":
            if ans[j][-1] == ans[j][1]:
                if ans[j][-1] == "S":
                    if s[-1] == "o":
                        if ans[j][-2] == ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                    if s[-1] == "x":
                        if ans[j][-2] != ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                if ans[j][-1] == "W":
                    if s[-1] == "o":
                        if ans[j][-2] != ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                    if s[-1] == "x":
                        if ans[j][-2] == ans[j][0]:
                            print(ans[j])
                            c += 1
                            break

        if ans[j][0] == "W":
            if ans[j][-1] != ans[j][1]:
                if ans[j][-1] == "S":
                    if s[-1] == "o":
                        if ans[j][-2] == ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                    if s[-1] == "x":
                        if ans[j][-2] != ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                if ans[j][-1] == "W":
                    if s[-1] == "o":
                        if ans[j][-2] != ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                    if s[-1] == "x":
                        if ans[j][-2] == ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
    if s[0] == "x":
        if ans[j][0] == "W":
            if ans[j][-1] == ans[j][1]:
                if ans[j][-1] == "S":
                    if s[-1] == "o":
                        if ans[j][-2] == ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                    if s[-1] == "x":
                        if ans[j][-2] != ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                if ans[j][-1] == "W":
                    if s[-1] == "o":
                        if ans[j][-2] != ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                    if s[-1] == "x":
                        if ans[j][-2] == ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
        if ans[j][0] == "S":
            if ans[j][-1] != ans[j][1]:
                if ans[j][-1] == "S":
                    if s[-1] == "o":
                        if ans[j][-2] == ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                    if s[-1] == "x":
                        if ans[j][-2] != ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                if ans[j][-1] == "W":
                    if s[-1] == "o":
                        if ans[j][-2] != ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
                    if s[-1] == "x":
                        if ans[j][-2] == ans[j][0]:
                            print(ans[j])
                            c += 1
                            break
if c == 0:
    print(-1)
