n = int(input())
s = input()

start = ["SS", "SW", "WS", "WW"]

for st in start:
    ans = st
    for i in range(1, n):
        if s[i] == "o" and ans[i] == "S":
            if ans[i - 1] == "S":
                ans += "S"
            else:
                ans += "W"
        elif s[i] == "x" and ans[i] == "S":
            if ans[i - 1] == "S":
                ans += "W"
            else:
                ans += "S"
        elif s[i] == "o" and ans[i] == "W":
            if ans[i - 1] == "S":
                ans += "W"
            else:
                ans += "S"
        elif s[i] == "x" and ans[i] == "W":
            if ans[i - 1] == "S":
                ans += "S"
            else:
                ans += "W"

    if ans[0] == ans[-1]:
        ans = ans[:n]
        ok = False
        if s[0] == "o" and ans[0] == "S":
            if ans[-1] == ans[1]:
                ok = True
        elif s[0] == "x" and ans[0] == "S":
            if ans[-1] != ans[1]:
                ok = True
        elif s[0] == "o" and ans[0] == "W":
            if ans[-1] != ans[1]:
                ok = True
        elif s[0] == "x" and ans[0] == "W":
            if ans[-1] == ans[1]:
                ok = True
        if ok:
            print(ans[:n])
            return
print(-1)
