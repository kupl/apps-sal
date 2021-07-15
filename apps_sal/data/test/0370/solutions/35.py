K = int(input())
x, y = map(int, input().split())

nowx, nowy = 0, 0
ans = []

def ok():
    nonlocal ans, x, y
    ans.append((x, y))
    print(len(ans))
    for (x, y) in ans:
        print(x,y)
    return
        


while(abs(nowx - x) + abs(nowy - y) >= 2*K):
    if x - nowx >= K:
        nowx += K
    elif nowx - x >= K:
        nowx -= K
    elif y - nowy >= K:
        nowy += K
    else:
        nowy -= K
    ans.append((nowx, nowy))

if (abs(nowx - x) + abs(nowy - y)) % 2 == 1 and K % 2 == 0:
    print(-1)
    return

    
if (abs(nowx - x) + abs(nowy - y)) == K:ok()
    
if (abs(nowx - x) + abs(nowy - y)) % 2 == 1:
    if abs(nowx+K - x) + abs(nowy - y) < 2*K:nowx += K
    elif abs(nowx-K - x) + abs(nowy - y) < 2*K:nowx -= K
    elif abs(nowx - x) + abs(nowy+K - y) < 2*K:nowy += K
    elif abs(nowx - x) + abs(nowy-K - y) < 2*K:nowy -= K
    ans.append((nowx, nowy))
    
if (abs(nowx - x) + abs(nowy - y)) == K:ok()

rest = K*2 - (abs(nowx-x) + abs(nowy-y))
rest //= 2
xgo, ygo = 1, 1

if nowx != x:
    xgo = (x - nowx) // abs(nowx - x)
if nowy != y:
    ygo = (y - nowy) // abs(nowy - y)

if abs(nowx-x) >= abs(nowy-y):
    nowx += xgo * (K - rest)
    nowy -= ygo * rest
    ans.append((nowx, nowy))
    
else:
    nowy += ygo * (K - rest)
    nowx -= xgo * rest
    ans.append((nowx, nowy))

ok()
