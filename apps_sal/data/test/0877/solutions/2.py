n, m = list(map(int,input().split()))
left = 0
right = n
for i in range(m):
    ui, vi = list(map(int,input().split()))
    if ui > vi:
        left = max(left,vi)
        right = min(right,ui)
    else:
        left = max(left,ui)
        right = min(right,vi)
if m == 0:
    right -= 1
if right > left:
    print(right-left)
else:
    print(0)

