
import sys

line = sys.stdin.readline()
line.strip()
comp = line.split(' ')
n = int(comp[0])
k = int(comp[1])

if(k*(k+1)//2 > n):
    print("-1")
    return

divs = []

d = 1
while(d*d <= n):
    if n%d == 0:
        divs.append(d)
        divs.append(n//d)
    d+=1

maxDiv = 0

for dv in divs:
    if (k+1)*k//2 <= dv:
        maxDiv = max(maxDiv,n//dv)
    if (k+1)*k//2 <= n//dv:
        maxDiv = max(maxDiv,dv)


arr = [maxDiv*x for x in range(1,k)] + [n-k*(k-1)//2*maxDiv]
print(" ".join(map(str,arr)))








