import sys
input = sys.stdin.readline
h,w,m = map(int,input().rstrip().split())
hw = [list(map(int,input().rstrip().split()))for _ in range(m)]

tate = [0]*(h+1)
yoko = [0]*(w+1)
bombpoint = set()

for x,y in hw:
    tate[x] += 1
    yoko[y] += 1
    bombpoint.add((x,y))

ans_x = []
ans_y = []
x_max = max(tate)
y_max = max(yoko)
for i in range(len(tate)):
    if tate[i] == x_max:
        ans_x.append(i)
for i in range(len(yoko)):
    if yoko[i] == y_max:
        ans_y.append(i)

ans = x_max + y_max
for x in ans_x:
    for y in ans_y:
        if (x,y) not in bombpoint:
            print(ans)
            return
print(ans - 1)
