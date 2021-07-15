from math import sqrt

eps = 1e-9

def mysqrt(x):
    if x <= 0:
        return 0
    return sqrt(x)

def good(R):
    nonlocal xs
    nonlocal ys
    nonlocal n
    
    left = -10**20
    right = 10**20
    
    for i in range(n):
        # (x - xi)**2 + (y - yi)**2 = R**2
        # y = R
        xi = xs[i]
        yi = abs(ys[i])
        
        D = 2 * R * yi - yi**2
        
        if D + eps < 0:
            return False
        
        sD = mysqrt(D)
        
        new_left = xi - sD
        new_right = xi + sD
        
        left = max(left, new_left)
        right = min(right, new_right)
        
        if left + eps > right:
            return False
    
    return True
        

def solve(lower, high, md):
    R = 0
    for _ in range(150):
        R = md(lower, high)
        
        if good(R):
            high = R
        else:
            lower = R
        
    return R

n = int(input())

xs = [0.0 for _ in range(n)]
ys = [0.0 for _ in range(n)]

for i in range(n):
    xs[i], ys[i] = list(map(float, input().split()))
    if i > 0:
        if ys[i] * ys[0] < 0:
            print(-1)
            return

R = None
if good(1):
    R = solve(0, 1, lambda x, y: (x + y) / 2)
else:
    R = solve(1, 1e16, lambda x, y: sqrt(x * y))

print('{:.16}'.format(R))

