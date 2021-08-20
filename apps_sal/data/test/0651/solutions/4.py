(n, m) = map(int, input().split())
a = []
startx = 0
starty = 0
for i in range(n):
    a.append(input())
    if 'S' in a[i]:
        startx = a[i].index('S')
        starty = i
s = input()
ans = 0
for l in range(4):
    for r in range(4):
        if r == l:
            continue
        for u in range(4):
            if u == r or u == l:
                continue
            for d in range(4):
                if d == u or d == r or d == l:
                    continue
                posx = startx
                posy = starty
                for i in s:
                    i = int(i)
                    if i == l:
                        posx -= 1
                    elif i == r:
                        posx += 1
                    elif i == d:
                        posy += 1
                    elif i == u:
                        posy -= 1
                    if posy < 0 or posy >= n or posx < 0 or (posx >= m):
                        break
                    elif a[posy][posx] == '#':
                        break
                    elif a[posy][posx] == 'E':
                        ans += 1
                        break
print(ans)
