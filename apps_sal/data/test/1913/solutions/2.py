n = int(input())
r = 1
l = 0
for a in input().split():
    u = 0
    for e in a:
        u += int(e)
    if u > 1:        
        r = a
    elif u == 0:
        l = -1
        break
    else:
        l += len(a) - 1
if l < 0:
    print(0)
else:
    print(r,'0' * l,sep = '')
    

