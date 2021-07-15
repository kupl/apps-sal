import math

def dis(a0, b0, x, y):
    return ((a0-x) ** 2 + (b0-y) ** 2) ** 0.5
    
# distance from point to segment
def minDistance(A, B, E) :  
   
    AB = [B[0] - A[0], B[1] - A[1]]  
    BE = [E[0] - B[0], E[1] - B[1]]
    AE = [E[0] - A[0], E[1] - A[1]]
  
    AB_BE = AB[0] * BE[0] + AB[1] * BE[1];  
    AB_AE = AB[0] * AE[0] + AB[1] * AE[1];  
  
    reqAns = 0;  
  
    # Case 1  
    if AB_BE > 0: 
        # Finding the magnitude  
        y = E[1] - B[1] 
        x = E[0] - B[0]  
        return (x * x + y * y) ** 0.5 
  
    # Case 2  
    elif (AB_AE < 0) : 
        y = E[1] - A[1] 
        x = E[0] - A[0]  
        return (x * x + y * y) ** 0.5
  
    # Case 3  
    else: 
        # Finding the perpendicular distance  
        x1, y1, x2, y2 = AB[0], AB[1], AE[0], AE[1]  
        mod    = (x1 * x1 + y1 * y1) ** 0.5
        
        return abs(x1 * y2 - y1 * x2) / mod
    
n, x0, y0 = map(int, input().split())
P    = [list(map(int, input().split())) for _ in range(n)]

max_ = 0
min_ = float("inf")

for i in range(n):
    p    = P[i]
    
    min_ = min(min_, minDistance(P[i], P[(i+1)%n], [x0, y0]))
    max_ = max(max_, dis(x0, y0, p[0], p[1]))
    
print(math.pi * (max_ * max_ - min_ * min_))
