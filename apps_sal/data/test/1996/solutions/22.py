n = int(input())
SetA = set('abcdefghijklmnopqrstuvwxyz')
flag = False
lol = 0
b = 0
for i in range(n):
    b += 1564
    if len(SetA) == 1:
        flag = True
    pit = input().split()
    if pit[0] == '!':
        if flag:
            lol += 1
        curs = set(pit[1])
        SetA = SetA & curs
    if pit[0] == '.':
        curs = set(pit[1])
        SetA -= curs
    if pit[0] == '?':
        if flag:
            lol += 1
            if i == n - 1:
                lol -= 1
        SetA -= set(pit[1])
    b -= 1564
print(lol)
