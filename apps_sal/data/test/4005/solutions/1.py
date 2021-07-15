w_x1, w_y1, w_x2, w_y2 = list(map(int, input().split()))

x1, y1, x2, y2 = list(map(int, input().split()))
if x1 <= w_x1 and w_x2 <= x2:
    if y1 <= w_y1: 
        w_y1 = max(y2, w_y1)
    if y2 >= w_y2: 
        w_y2 = min(y1, w_y2)  

if y1 <= w_y1 and w_y2 <= y2:
    if x1 <= w_x1: 
        w_x1 = max(x2, w_x1)
    if x2 >= w_x2: 
        w_x2 = min(x1, w_x2) 
        
x1, y1, x2, y2 = list(map(int, input().split()))
if x1 <= w_x1 and w_x2 <= x2:
    if y1 <= w_y1: 
        w_y1 = max(y2, w_y1)
    if y2 >= w_y2: 
        w_y2 = min(y1, w_y2)  

if y1 <= w_y1 and w_y2 <= y2:
    if x1 <= w_x1: 
        w_x1 = max(x2, w_x1)
    if x2 >= w_x2: 
        w_x2 = min(x1, w_x2) 
        

if w_x1 >= w_x2 and w_y1 >= w_y2:
    print("NO")
else:
    print("YES")


