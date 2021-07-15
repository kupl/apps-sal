import sys
f = sys.stdin

n, m  = map(int, f.readline().strip().split())

res = True
for i in range(m):
   d, h  = map(int, f.readline().strip().split()) 
   if i==0:
       maxH = h + (d - 1)
       hpr = h
       dpr = d
   else: 
       if abs(h-hpr)>(d-dpr):
           res = False
       else:
           dt = d - dpr - (max(hpr, h) - min(hpr, h))
           maxH = max(maxH, max(hpr, h) + (dt // 2))
           hpr = h
           dpr = d       

maxH = max(maxH, hpr + (n - dpr))

       
if res:
    print(maxH)  
else :
    print('IMPOSSIBLE')
