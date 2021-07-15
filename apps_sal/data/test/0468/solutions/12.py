import math;
def getIntList():
    return list(map(int, input().split()));
def getTransIntList(n):
    first=getIntList();
    m=len(first);
    result=[[0]*n for _ in range(m)];
    for i in range(m):
        result[i][0]=first[i];
    for j in range(1, n):
        curr=getIntList();
        for i in range(m):
            result[i][j]=curr[i];
    return result;
x, y=getIntList();
left=y*math.log(x);
right=x*math.log(y);
if left<right:
    print('<')
elif left>right:
    print('>');
else:
    print('=');
