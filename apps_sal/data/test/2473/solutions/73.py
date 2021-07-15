from sys import stdin
def main():
    #入力
    readline=stdin.readline
    inf=10**20
    n,k=map(int,readline().split())
    co=[list(map(int,readline().split())) for _ in range(n)]
    
    co.sort()
    
    x_range=[]
    for i in range(n-1):
        for j in range(i+1,n):
            x_range.append((co[i][0],co[j][0]))

    co.sort(key=lambda x:x[1])
    ans=inf
    for x in x_range:
        x_min=x[0]
        x_max=x[1]
        y_min=0
        y_max=0
        for under in range(n):
            cnt=0
            for i in range(under,n):
                if x_min<=co[i][0]<=x_max:
                    if cnt==0:
                        y_min=co[i][1]
                        cnt+=1
                    else:
                        y_max=co[i][1]
                        cnt+=1
                if cnt==k:
                    break
            if cnt==k:
                ans=min(ans,(x_max-x_min)*(y_max-y_min))

    print(ans)

def __starting_point():
    main()
__starting_point()
