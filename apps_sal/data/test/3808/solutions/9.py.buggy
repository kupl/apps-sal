N = int(input())
S = list(input())

lnum = len([x for x in S if x == "("])
rnum = len([x for x in S if x == ")"])
if lnum != rnum:
    print("No")
    return

lcnt = 0
rcnt = 0
for x in S:
    if x == "(":
        lcnt += 1
    else:
        if lcnt > 0:
            lcnt -= 1
        else:
            rcnt += 1

if rcnt > 1:
    print("No")
else:
    print("Yes")
