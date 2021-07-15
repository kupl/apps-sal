u = 1000000007
import sys
def P(n): 
    #take first edge or no? depth == < - >
    X = [[0 for i in range(2*n+1)] for j in range(2*n+1)]
    X[0][0] = 1
    r = 0
    for i in range(1,2*n+1):
        X[i][0]=X[i-1][1]
        for j in range(1,min([2*n+1-i,i+1])):
            X[i][j] = (X[i-1][j+1]+X[i-1][j-1])%u
        if i%2:r+=sum(X[i])
    return r%u

print(P(int(sys.stdin.read()[:-1])))

