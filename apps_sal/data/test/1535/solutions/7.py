import sys
f = sys.stdin

n, x0, y0 = map(int, f.readline().strip().split())

xy = []
for i in range(n):
    xy.append( list(map(int, f.readline().strip().split())) )

used = [0]*n
v = 0
for i in range(n):
    if used[i]==0:
        v += 1
        used[i] = 1
        kx = x0 - xy[i][0]
        ky = y0 - xy[i][1]
        if kx<0:
            kx *= -1
            ky *= -1
        if kx==0 and ky<0:
            ky *= -1
        for j in range(i,n):
            if used[j]==0:    
                kxj = x0 - xy[j][0]
                kyj = y0 - xy[j][1]                
                if kxj<0:
                    kxj *= -1
                    kyj *= -1
                if kxj==0 and kyj<0:
                    kyj *= -1
                if kx*kyj==ky*kxj:
                    used[j] = 1
print(v)
