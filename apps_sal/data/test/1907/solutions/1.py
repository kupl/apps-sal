from sys import stdin, stdout
import math

def dist(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

# Is b inside a
def inside(a,b):
    if dist(b,a)<a[2]:
        return True
    else:
        return False

n = int(stdin.readline().rstrip())
pointList=[]
for _ in range(n):
    x,y,r = list(map(int,stdin.readline().rstrip().split()))
    pointList.append((x,y,r))
    
pointList.sort(key = lambda x: x[2],reverse=True)
positiveCounter = [0]*n
group = [0]*n
parent = [-1]*n

spaciousness=0
for i in range(n):
    contained = -1
    for j in range(i-1,-1,-1):
        if inside(pointList[j],pointList[i]):
            contained=j
            break
    if contained<0:
        positiveCounter[i]=1
        group[i]=1
        spaciousness+=math.pi*pointList[i][2]*pointList[i][2]
    else:
        parent[i]=j
        group[i] = 3-group[j]
        if parent[j]>=0:
            positiveCounter[i] = positiveCounter[j]*-1
            spaciousness+=math.pi*pointList[i][2]*pointList[i][2]*positiveCounter[i]
        else:
            positiveCounter[i]=1
            spaciousness+=math.pi*pointList[i][2]*pointList[i][2]*positiveCounter[i]

print(spaciousness)

