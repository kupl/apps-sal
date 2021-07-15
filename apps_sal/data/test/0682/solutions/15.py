
def rook(r1,c1,r2,c2):
    if r1==r2 or c1==c2:
        return 1
    else:
        return 2

def bishop(r1,c1,r2,c2):
    s1 = r1+c1
    s2 = r2+c2
    if (s1%2==0 and s2%2!=0) or (s1%2!=0 and s2%2==0):
        return 0
    elif abs(r1-r2)==abs(c1-c2):
        return 1
    else:
        return 2

def king(r1,c1,r2,c2):
    mine = abs(r1-r2)+abs(c1-c2)
    #move horizonatal
    for i in range(1,9):
        if abs(i-r2)==abs(c1-c2):
            mine = min(mine,abs(i-r1)+abs(c1-c2))
    for i in range(1,9):
        if abs(i-c2)==abs(r1-r2):
            mine = min(mine,abs(i-c1)+abs(r2-r1))
    return mine

s = input().split()
r1 = int(s[0])
c1 = int(s[1])
r2 = int(s[2])
c2 = int(s[3])
ans = str(rook(r1,c1,r2,c2))+" "+str(bishop(r1,c1,r2,c2))+" "+str(king(r1,c1,r2,c2))
print(ans)

