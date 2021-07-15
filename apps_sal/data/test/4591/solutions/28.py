import math
a, b, c, x, y = list(map(int, input().split(' ')))
ans = float('inf')
c = c*2
for i in range(max(x, y)+1):
    ans = min(ans, a*max(0, x-i)+b*max(0,y-i)+c*i)
print(ans)

