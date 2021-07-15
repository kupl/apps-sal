import math


a, b = [int(i) for i in input().split()]
n = int(input())
t = 10 ** 9
for i in range(n):
    x, y, v = [int(j) for j in input().split()]
    t = min(t, ((abs(a - x) ** 2 + abs(b - y) ** 2) ** 0.5) / v)
print(t)
    
    
    

