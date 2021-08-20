from sys import stdin, stdout
doomed = False
(n, m) = list(map(int, stdin.readline().rstrip().split()))
for _ in range(m):
    groupInfo = [int(a) for a in stdin.readline().rstrip().split()]
    groupSet = set()
    doomGroup = True
    for i in groupInfo[1:]:
        if -i in groupSet:
            doomGroup = False
            break
        else:
            groupSet.add(i)
    if doomGroup:
        doomed = True
if doomed:
    print('YES')
else:
    print('NO')
