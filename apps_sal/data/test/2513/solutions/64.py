n = int(input())
s = input()
s += s[0]
lst = ["SS", "SW", "WS", "WW"]
for x in lst:
    ans = x
    for i in range(1, n + 1):
        if (s[i] == "o" and ans[i] == "S") or (s[i] == "x" and ans[i] == "W"):
            if ans[i - 1] == "S":
                ans += "S"
            else:
                ans += "W"
        else:
            if ans[i - 1] == "S":
                ans += "W"
            else:
                ans += "S"
    if ans[-2:] == x:
        print(ans[:n])
        return
print(-1)
