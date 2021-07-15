n = int(input())
s = set("abcdefghijklmnopqrstuvwxyz")
mark = False
cnt = 0
for i in range(n):
    if len(s) == 1:
        mark = True
    tmp = input().split()
    if tmp[0] == "!":
        if mark:
            cnt += 1
        curs = set(tmp[1])
        s = s & curs
    if tmp[0] == ".":
        curs = set(tmp[1])
        s -= curs
    if tmp[0] == "?":
        if mark:
            cnt += 1
            if i == n - 1:
                cnt -= 1
        s -= set(tmp[1])
print(cnt)

