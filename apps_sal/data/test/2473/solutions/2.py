import sys
input = sys.stdin.readline
INF = 10**20
MOD = 10**9 + 7
from bisect import insort_left

def main():
    n,k = map(int,input().split())
    XY = [tuple(map(int,input().split())) for _ in range(n)]  
    XY.sort(key = lambda x:x[0])
    
    ans = INF
    for l in range(n - k + 1):
        Y = [XY[i][1] for i in range(l,l + k - 1)]
        Y.sort()
        dif = -1
        for r in range(l + k - 1, n):
            dif += 1
            insort_left(Y,XY[r][1])
            w = INF
            for i in range(dif + 1):
                w = min(w, Y[i + k - 1] - Y[i])
            ans = min(ans, w * (XY[r][0] - XY[l][0]))
    
    print(ans)   

def __starting_point():
    main()
__starting_point()
