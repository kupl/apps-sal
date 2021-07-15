import sys

def vert(f, d, c, h):
    f[d][c] = '+'
    f[h-1-d][c] = '+'
    for i in range(d+1,h-1-d):
        f[i][c] = '|'
    return f

n = int(input())
s = sys.stdin.readline().rstrip()

d = 0
maxd=1
for c in s:
    if c == '[':
        d+=1
        if d>maxd:
            maxd=d
    else:
        d-=1

h = 2*maxd +1
opcl = s.count("[]")

w = opcl*5 + (len(s) - opcl*2)

f = [[' ']*w for _ in range(h)]

d = 0
c = 0
for i in range(n):
    if s[i] == '[':        
        f = vert(f,d,c,h)
        f[d][c+1] = '-'
        f[h-1-d][c+1] = '-'        
        d+=1
    else:
        if i>0 and s[i-1] == '[':
            c+=3
        d-=1
        f = vert(f,d,c,h)
        f[d][c-1] = '-'
        f[h-1-d][c-1] = '-'
        
    c+=1

ans = ["".join(x) for x in f]
print("\n".join(ans))

