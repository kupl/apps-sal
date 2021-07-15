import math
def solve(c,hr,hb,wr,wb):
    INF = math.ceil(math.sqrt(c))
    if wb > wr:
        wb,wr = wr,wb
        hb,hr = hr,hb
    if wr > INF:
        ans = 0
        i = 0
        while i * wr <= c and i < INF:
            ans = max(ans,i * hr + ((c - i * wr) // wb) * hb)
            i+=1
        return ans
    else:
        if wr * hb > hr * wb:
            wb,wr = wr,wb
            hb,hr = hr,hb
        ans = 0
        j = 0
        while j * wb <= c and j <= wr:
            ans = max(ans,j * hb + ((c - j * wb) // wr) * hr)
            j+=1
        return ans

c,hr,hb,wr,wb = list(map(int,input().split()))
print(solve(c,hr,hb,wr,wb))

