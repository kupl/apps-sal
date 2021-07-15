

d = {}
for i in range(22):
    d[i] = {}
n,m,k = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(n)]
def check(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    else:
        return True

def go(x,y,now):
    if check(x,y) == False:
        return

    now ^= l[x][y]
    if x + y == m - 1:
        #print('yes')
        if now in d[x]:
            d[x][now] += 1
        else:
            d[x][now] = 1
        return

    go(x+1,y,now)
    go(x,y+1,now)

re = 0
def goRev(i,j,now):
    if check(i,j) == False:
        return

    if i + j == m - 1:
        cur = k ^ now
        if cur in d[i]:
            nonlocal re
            #print(ans)
            re += d[i][cur]
        return

    now ^= l[i][j]
    goRev(i-1,j,now)
    goRev(i,j-1,now)


go(0, 0, 0)
goRev(n-1, m-1, 0)
#print(d)
print(re)
