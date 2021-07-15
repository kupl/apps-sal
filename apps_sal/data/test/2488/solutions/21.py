def main():
    import sys
    input=sys.stdin.readline
    l=lambda: list(map(int,input().split()))
    n,d,a=l()
    xh=[]
    for i in range(n):
        xi,hi=l()
        xh.append([xi,hi])
    xh.sort()
    
    
    right_index=[]
    
    #尺取り法
    tmp=0
    for i in range(n):
        j=tmp
        while xh[j][0]<=xh[i][0]+2*d:
            j+=1
            if j==n: break
        j-=1
        right_index.append(j)
        tmp=j

    
    ans=0
    cnt=0
    damage=[0]*(n+1)
    for i in range(n):
    	xh[i][1]-=(ans-cnt)*a
    	damage_cnt=max(0,(xh[i][1]-1)//a + 1)
    	ans+=damage_cnt
    	damage[right_index[i]]+=damage_cnt
    	cnt+=damage[i]
    print(ans)

def __starting_point():
    main()
__starting_point()
