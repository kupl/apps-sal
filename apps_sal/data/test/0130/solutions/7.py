import sys

def main():
    n,m = list(map(int,sys.stdin.readline().split()))
    x=[]
    for i in range(n):
        x.append(sys.stdin.readline().rstrip())

    y = [-1,-1,-1,-1]

    for i in range(n):
        for j in range(m):
            if x[i][j]=='B':
                if y[0]==-1:
                    y[0]=i
                y[1]=max(y[1],j)
                y[2] = max(y[2],i)
                if y[3]!=-1:
                    y[3] = min(y[3],j)
                else:
                    y[3] = j

    if y[0] == -1 and y[1] == -1 and y[2] == -1 and y[3] == -1:
        print(1)
        return 

    q = max(y[1]-y[3]+1, y[2]-y[0]+1)
    if q > m or q>n:
        print(-1)
        return

    ans = 0
    for i in range(y[0],y[2]+1):
        for j in range(y[3],y[1]+1):
            if x[i][j]=='W':
                ans+=1

    ans+= q*(q - (y[2]-y[0]+1)) + q*(q - (y[1]-y[3]+1)) 
    print(ans)

    
main()

