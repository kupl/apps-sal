n = int(input())
x1, x2 = list(map(int, input().split(" ")))

def intercepts(k, b):
    y1 = k*x1+b
    y2 = k*x2+b
    return [y1, y2]

inter=[]
for i in range (n):
    k, b = list(map(int, input().split(" ")))
    inter += [intercepts(k, b)]

inter.sort()
right=[]

for i in range (n):
    intercept = inter[i]
    right += [intercept[1]]
    
right2=[]
for thing in right:
    right2+=[thing]
right.sort()

if right == right2:
    print("NO")
else:
    print("YES")


