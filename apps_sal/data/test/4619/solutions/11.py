w, h, n = map(int,input().split())
L = [list(map(int,input().split())) for i in range(n)]
x1 = 0
x2 = w
y1 = 0
y2 = h
for i in range(n):
    if L[i][2] == 1:
        x1 = max(L[i][0], x1)
    if L[i][2] == 2:
        x2 = min(L[i][0], x2)
    if L[i][2] == 3:
        y1 = max(L[i][1], y1)
    if L[i][2] == 4:
        y2 = min(L[i][1], y2)
        
ans = 0
if x2>=x1 and y2>=y1:
    ans = (x2-x1)*(y2-y1)
print(ans)
