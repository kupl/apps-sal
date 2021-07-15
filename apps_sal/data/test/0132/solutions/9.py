n = int(input())
pieces = [int(x) for x in input().split()]
sm = 360
curs = 0
ans = []
for i in range(n):
    for elem in pieces:
        ans.append(abs(sm - 2 * curs))
        curs += elem
        if curs >= 360:
            curs = 0
    pieces.append(pieces.pop(0))
print(min(ans))
