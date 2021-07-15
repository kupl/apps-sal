import math
s = input()
s = int(s)
n = 0
for i in range(1,10000):
    n+=i
    s-=n
    if s<0:
        ans = i-1
        break
print(ans)

