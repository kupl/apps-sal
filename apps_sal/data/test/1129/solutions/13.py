numPoints = int(input())
points = list(map(int, input().split(" ")))
points.sort()

def calcVal(point, points):
    tally = 0
    for i in range(len(points)):
        tally += abs(points[i] - point)
    return tally

if len(points)%2==0:
    leftDex = len(points)//2 -1
    rightDex = len(points)//2
    '''values = [calcVal(points[leftDex], points), calcVal(points[rightDex], points)]
    minVal = min(values)
    which = values.index(minVal)
    if which == 0:
        print(points[leftDex])
    else:
        print(points[rightDex])'''
    print(points[leftDex])
else:
    index = len(points)//2
    print(points[index])
    

