from math import sqrt
n = int(input())
x = int(sqrt(2*n))
while x*(x+1) <= 2*(n+1):
    x += 1
x -= 1
print(n+1-x)
