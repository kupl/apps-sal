from math import sqrt
def solve(n):
    z = 2*(n+1)
    y = int(sqrt(z))
    if y*(y+1) > z:
        y -= 1
    return n - y + 1

n = int(input())
print(solve(n))
