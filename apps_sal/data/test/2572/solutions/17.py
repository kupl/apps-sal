from collections import defaultdict as dd, deque,Counter
t = int(input())

for _ in range(t):
    n,m = list(map(int,input().split()))
    A = [[int(x) for x in input().split()] for _ in range(n)]
    
    cost = 0
    for i in range(n):
        for j in range(m):
            ix = {(i,j), (n-i-1,j), (i,m-j-1), (n-i-1,m-j-1)}
            vals = sorted([A[i][j] for i,j in ix])
            b = vals[len(vals)//2]
            cost += sum(abs(a-b) for a in vals)
            A[i][j] = A[n-i-1][j] = A[i][m-j-1] = A[n-i-1][m-j-1] = b
    print(cost)



