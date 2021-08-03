n = int(input())
string = input()
res = []
r = 0
for i in string:
    if i not in res:
        if len(res) == 2 or len(res) == 0:
            res = [i]
            r += 1
        else:
            if (res[0] in ("U", "D") and i in ("L", "R")) or (i in ("U", "D") and res[0] in ("L", "R")):
                res.append(i)
            else:
                res = [i]
                r += 1

print(r)
