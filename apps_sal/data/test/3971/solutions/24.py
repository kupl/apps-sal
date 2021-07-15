import sys

k = [0] * 100001
n = int(sys.stdin.readline())
st = [int(x) for x in (sys.stdin.readline()).split()]

for i in st:
    k[i] += 1
    
x = 0
y = 0

j = 100000
while(j > 0):
    if(j % 2 != 0):
        x = max(x + k[j] * j, y)
    else:
        y = max(y + k[j] * j, x)
    j -= 1
        
print(max(x, y))
