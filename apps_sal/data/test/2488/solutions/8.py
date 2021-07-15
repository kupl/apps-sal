from collections import deque
n , d , a = map(int,input().split())
mon = [tuple(map(int,input().split())) for i in range(n)]
mon.sort()
p = deque(mon)
baku = deque()
cou = 0
ans = 0
while p:
    nowx , nowh = p.popleft()
    while baku:
        bx , bh = baku.popleft()
        if bx >= nowx:
            baku.appendleft((bx,bh))
            break
        elif bx < nowx:
            cou -= bh
    if nowh <= cou:
        continue
    elif nowh > cou:
        k = -((-nowh+cou)//a)
        ans += k
        cou += a*k
        baku.append((nowx+2*d,a*k))
print(ans)
