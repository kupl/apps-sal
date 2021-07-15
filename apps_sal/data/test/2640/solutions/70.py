from sys import stdin
import numpy as np
def main():
    #入力
    readline=stdin.readline
    h,w=map(int,readline().split())
    grid=[readline().strip() for _ in range(h)]
    grid=[[1 if grid[i][j]=="." else 0 for j in range(w)] for i in range(h)]
    grid=np.array(grid,dtype=np.int64)

    up=np.zeros((h,w),dtype="int64")
    up[0]=grid[0]
    for i in range(1,h):
        up[i]=(up[i-1]+1)*grid[i]
    
    down=np.zeros((h,w),dtype="int64")
    down[-1]=grid[-1]
    for i in range(h-2,-1,-1):
        down[i]=(down[i+1]+1)*grid[i]
    
    left=np.zeros((h,w),dtype="int64")
    left[:,0]=grid[:,0]
    for i in range(1,w):
        left[:,i]=(left[:,i-1]+1)*grid[:,i]
    
    right=np.zeros((h,w),dtype="int64")
    right[:,-1]=grid[:,-1]
    for i in range(w-2,-1,-1):
        right[:,i]=(right[:,i+1]+1)*grid[:,i]

    ans=(up+down+left+right-3).max()
    print(ans)
    
def __starting_point():
    main()
__starting_point()
