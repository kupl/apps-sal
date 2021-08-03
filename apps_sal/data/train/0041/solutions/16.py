t = int(input())
for i3 in range(t):
    n, k = map(int, input().split())
    inp = str(input())
    s, ans, x = [], [], []
    for i in range(n):
        x.append(inp[i])
    for i in range(k - 1):
        s.append("(")
        s.append(")")
    for i in range(n // 2 - k + 1):
        s.append("(")
    for i in range(n // 2 - k + 1):
        s.append(")")
    for i in range(n):
        if x[i] == s[i]:
            pass
        else:
            temp = []
            for i2 in range(i, n):
                temp.append(x[i])
                if x[i2] == s[i]:
                    ans.append([i + 1, i2 + 1])
                    temp.reverse()
                    for i3 in range(i, i2 + 1):
                        x[i3] = temp[i3 - i]
                    break
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
