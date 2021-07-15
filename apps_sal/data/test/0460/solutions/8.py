from sys import stdin, stdout
from math import ceil

p, x, y = map(int, stdin.readline().split())
s = set()


if x < y:
    ans = (y - x) // 100
    x = x + 100 * ans
else:
    ans = 0
    
if x >= y:
    label = 0
    for i in range(100):
        xc = x + 100 * i
        
        while (xc >= y):
            if (not xc in s):
                s.add(xc)
            
                ind = (xc // 50) % 475
        
                for j in range(25):
                    ind = (ind * 96 + 42) % 475
                    
                    if ind + 26 == p:
                        label = 1
                        ans += i
                
                if label:
                    break
            elif i:
                break
        
            xc -= 50
        
        if label:
            break

stdout.write(str(ans))
