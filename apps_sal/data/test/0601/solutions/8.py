
from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    p,f = list(map(int,stdin.readline().split()))
    cs,cw = list(map(int,stdin.readline().split()))
    s,w = list(map(int,stdin.readline().split()))

    if s > w:
        cs,cw = cw,cs
        s,w = w,s

    ans = 0
    for ps in range(cs+1):

        if ps * s > p:
            break

        pw = min(cw , (p-ps*s)//w)

        fs = min( cs-ps , f//s )
        fw = min( cw-pw , (f-fs*s)//w )
        ans = max(ans , ps+pw+fs+fw)

    print (ans)

