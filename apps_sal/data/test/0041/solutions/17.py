import math
n = int(input())
data = []
data = list(map(int,input().split()))
l = [0] * n
r = [0] * n
p = 2 * n
p1 = 2 * n
s = ''
for i in range(n):
    l[i] = p
    if data[i] == 0:
        p = i
    
for i in range(n - 1,-1, -1):
    r[i] = p1
    if data[i] == 0:
        p1 = i 

for i in range(n): 
    if data[i] != 0:
        print(min(abs((l[i] - i)),abs((r[i] - i))), end = ' ')
    else:
        print(0, end = ' ')
        

    
