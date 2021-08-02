def is_num(s):
    if len(s) == 0:
        return False
    if s[0] == '0' and len(s) > 1:
        return False
    for i in s:
        c = str(i)
        if not c.isdigit():
            return False
    return True


a = list(input().split(sep=","))
b = []
for i in a:
    t = list(i.split(sep=";"))
    for j in t:
        b.append(j)
ans = []
ans2 = []
for i in range(len(b)):
    if is_num(b[i]):
        ans.append(b[i])
        b[i] = "*"
    else:
        ans2.append(b[i])
if len(ans) == 0:
    print("-")
else:
    print("\"", end="")
    print(*ans, sep=",", end="")
    print("\"")
if len(ans2) == 0:
    print("-")
else:
    print("\"", end="")
    print(*ans2, sep=",", end="")
    print("\"")
