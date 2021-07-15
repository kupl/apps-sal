import sys

t, sx, sy, ex, ey = list(map(int,input().split()))

inp = input()
movu, movd, movf, movb,dontx, donty = 0, 0, 0, 0, 0, 0

if sx < ex:
    movf = True  
else:
    movb = True 

if ex == sx : dontx = True 

if sy < ey:
    movu = True  
else:
    movd = True 

if ey == sy : donty = True

t = 0  
for c in inp:
    t = t + 1 
    if c == 'S':
        if donty:
            continue 
        if movd:
            sy -= 1 
            if sy == ey: donty = True
    elif c == 'E':
        if dontx: continue 
        if movf:
            sx += 1
            if sx == ex: dontx = True 
    elif c == 'N':
        if donty : continue 
        if movu:
            sy += 1
            if sy == ey: donty = True
    elif c == 'W':
        if dontx: continue 
        if movb:
            sx -= 1
            if sx == ex: dontx = True 

    if sx == ex and sy == ey:
        print(t)
        return

print("-1")

