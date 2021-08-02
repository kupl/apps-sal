n = int(input())
soot = set()
usoot = set()
a = list(map(int, input().split()))
ans = []
f = True
c = 0
for i in a:
    c += 1
    if i < 0:
        if -i in soot:
            soot.remove(-i)
            usoot.add(-i)
        else:
            f = False
            break
    else:
        if i in soot or i in usoot:
            f = False
            break
        else:
            soot.add(i)
    if len(soot) == 0:
        usoot = set()
        ans.append(c)
        c = 0
if len(soot) != 0:
    f = False
if f:
    print(len(ans))
    for i in ans:
        print(i, end=" ")
else:
    print(-1)
