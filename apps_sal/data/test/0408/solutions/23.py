#print(sum(map(int, input().split())) // 3)
import math
n, m = list(map(int, input().split()))
x = (2 * m - n) / 3
y = (2 * n - m) / 3
if x >= 0 and y >= 0:
    print((n + m) // 3)
elif x >= 0 and y <= 0:
    print(n)
else:
    print(m)
    

