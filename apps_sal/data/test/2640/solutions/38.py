from sys import stdin
import numpy as np
def main():
    #入力
    readline=stdin.readline
    h,w=map(int,readline().split())
    grid=[readline().strip() for _ in range(h)]
    grid2=np.zeros((h,w),dtype="int64")
    for i in range(h):
        for j in range(w):
            if grid[i][j]==".":
                grid2[i][j]=1
            else:
                grid2[i][j]=0

    up=np.zeros((h,w),dtype="int64")
    up[0]=grid2[0]
    for i in range(1,h):
        up[i]=(up[i-1]+1)*grid2[i]
    
    down=np.zeros((h,w),dtype="int64")
    down[-1]=grid2[-1]
    for i in range(h-2,-1,-1):
        down[i]=(down[i+1]+1)*grid2[i]
    
    left=np.zeros((h,w),dtype="int64")
    left[:,0]=grid2[:,0]
    for i in range(1,w):
        left[:,i]=(left[:,i-1]+1)*grid2[:,i]
    
    right=np.zeros((h,w),dtype="int64")
    right[:,-1]=grid2[:,-1]
    for i in range(w-2,-1,-1):
        right[:,i]=(right[:,i+1]+1)*grid2[:,i]

    ans=(up+down+left+right-3).max()
    print(ans)
    
def __starting_point():
    main()
__starting_point()
