def main():
    import sys
    import numpy as np

    def input(): return sys.stdin.readline().rstrip()

    h, w = map(int, input().split())
    g = np.zeros((h, w), dtype=int)
    for i in range(h):
        g[i] = [int(s == '.') for s in input()]
    
    L = g.copy()
    R = g.copy()
    U = g.copy()
    D = g.copy()
    
    for i in range(1,h):
        U[i] = (U[i-1]+1)*g[i]
        D[~i] = (D[~i+1]+1)*g[~i]
    for j in range(1, w):
        L[:, j] = (L[:, j-1]+1)*g[:,j]
        R[:, ~j] = (R[:, ~j+1]+1)*g[:, ~j]
     
    ans = np.max(L+R+U+D-3)
    print(ans)
            
                
def __starting_point():
    main()
__starting_point()
