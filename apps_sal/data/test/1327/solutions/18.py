import sys
import numpy as np
input = sys.stdin.readline
def main():
    n,m = map(int,input().split())
    xyz = [[] for _ in range(8)]
    pm = [[ 1, 1, 1],
          [ 1, 1,-1],
          [ 1,-1, 1],
          [-1, 1, 1],
          [ 1,-1,-1],
          [-1, 1,-1],
          [-1,-1, 1],
          [-1,-1,-1]]
    pm = np.array(pm)
    for _ in range(n):
        x,y,z = map(int,input().split())
        for i in range(8):
            k = np.array([x,y,z])
            xyz[i].append(sum(pm[i]*k))
    ans = -10**20
    for i in range(8):
        X = xyz[i]
        X.sort(reverse=True)
        cnt = 0
        for j in range(m):
            cnt += X[j]
        ans = max(ans,cnt)
    print(ans)

def __starting_point():
    main()
__starting_point()
