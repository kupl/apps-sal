n = int(input())
s = list(input())
u = ["S", "W"]
for i in range(2):
    for j in range(2):
        ans = [0] * n
        ans[0] = u[i]
        ans[1] = u[j]
        for k in range(2, n):
            if s[k - 1] == "o":
                if ans[k - 1] == "S":
                    if ans[k - 2] == "S":
                        c = 0
                    else:
                        c = 1
                else:
                    if ans[k - 2] == "S":
                        c = 1
                    else:
                        c = 0
            else:
                if ans[k - 1] == "S":
                    if ans[k - 2] == "S":
                        c = 1
                    else:
                        c = 0
                else:
                    if ans[k - 2] == "S":
                        c = 0
                    else:
                        c = 1
            ans[k] = u[c]
        m = 0
        if s[0] == "o":
            if ans[0] == "S":
                if ans[1] == ans[n - 1]:
                    m += 1
            else:
                if ans[1] != ans[n - 1]:
                    m += 1
        else:
            if ans[0] == "W":
                if ans[1] == ans[n - 1]:
                    m += 1
            else:
                if ans[1] != ans[n - 1]:
                    m += 1
        if s[n - 1] == "o":
            if ans[n - 1] == "S":
                if ans[0] == ans[n - 2]:
                    m += 1
            else:
                if ans[0] != ans[n - 2]:
                    m += 1
        else:
            if ans[n - 1] == "W":
                if ans[0] == ans[n - 2]:
                    m += 1
            else:
                if ans[0] != ans[n - 2]:
                    m += 1
        if m == 2:
            print("".join(ans))
            return
print(-1)
