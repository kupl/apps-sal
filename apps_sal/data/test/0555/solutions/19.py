import sys
f = sys.stdin

s = f.readline().strip()

p = ''
start = 0
for u in s:
    #print(u,s) 
    m = int(u)
    if m>4 and start>0 or m>4 and m<9 and start==0: 
        m = 9 - m
    if start>0:
        p = p + str(m)
    elif  m>0:    
        p = p + str(m)
    
    start += 1
    #print(u, p)
    
print(p)    
