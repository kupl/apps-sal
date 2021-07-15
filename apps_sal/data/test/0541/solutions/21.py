n,m=map(int,input().split())
R=[]
for i in range (m) :
    a,b=map(int,input().split())
    R.append ([b, a])
R.sort()

def solve() :
    ans,t=0,0
    for i in range (m) :
        if t<=R[i][1]:
            ans+=1
            t=R[i][0]
    return ans
print (solve ())
