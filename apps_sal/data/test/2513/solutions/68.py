N = int(input())
S = input()

for i in range(4):
    ans = [0] * N
    if i == 0:
        ans[-1] = "S"
        ans[0] = "S"
    elif i == 1:
        ans[-1] = "S"
        ans[0] = "W"
    elif i == 2:
        ans[-1] = "W"
        ans[0] = "S"
    else:
        ans[-1] = "W"
        ans[0] = "W"

    for j, s in enumerate(S):
        if j != N - 1 and j != N - 2:
            if ans[j] == "S":
                if s == "o":
                    ans[j + 1] = ans[j - 1]
                else:
                    if ans[j - 1] == "S":
                        ans[j + 1] = "W"
                    else:
                        ans[j + 1] = "S"
            else:
                if s == "x":
                    ans[j + 1] = ans[j - 1]
                else:
                    if ans[j - 1] == "S":
                        ans[j + 1] = "W"
                    else:
                        ans[j + 1] = "S"
        elif j == N - 2:
            flag = 0
            if ans[N - 2] == "S":
                if s == "o":
                    if ans[N - 1] == ans[N - 3]:
                        flag = 1
                else:
                    if ans[N - 1] != ans[N - 3]:
                        flag = 1
            else:
                if s == "x":
                    if ans[N - 1] == ans[N - 3]:
                        flag = 1
                else:
                    if ans[N - 1] != ans[N - 3]:
                        flag = 1
        elif flag:
            if ans[N - 1] == "S":
                if s == "o":
                    if ans[N - 2] == ans[0]:
                        print(("".join(ans)))
                        return
                else:
                    if ans[N - 2] != ans[0]:
                        print(("".join(ans)))
                        return
            else:
                if s == "x":
                    if ans[N - 2] == ans[0]:
                        print(("".join(ans)))
                        return
                else:
                    if ans[N - 2] != ans[0]:
                        print(("".join(ans)))
                        return
print((-1))
