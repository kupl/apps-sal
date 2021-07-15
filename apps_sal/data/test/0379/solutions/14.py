# You lost the game.

n,m = list(map(int, input().split()))
L = [str(input()) for _ in range(n)]

x = y = ok = 0
for i in range(n):
    for j in range(m):
        if L[i][j] == 'X':
            x = i
            y = j
            ok = 1
            break
    if ok:
        break
l = y
while l < m and L[x][l] == 'X':
    l += 1

ok = 0
att = 0
for i in range(x+1, n):
    vu = 0
    for j in range(m):
        if L[i][j] == 'X':
            vu = 1
            if j < y or j >= l or att:
                ok = -1
                break
        else:
            if vu and j >= y and j < l:
                ok = -1
                break
            elif j >= y and j < l:
                att = 1
    if ok or vu == 0:
        break

if ok == -1:
    print("NO")
else:
    print("YES")



        

