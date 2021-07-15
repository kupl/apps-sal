def count(a,b,c,d):
    return sum([arr[i][j] for i in range(a,c + 1) for j in range(b,d + 1)])

def solve(r,c,n,m):
    ans = 0
    for i in range(1,r + 1):
        for j in range(1,c + 1):
            for k in range(i,r + 1):
                for l in range(j,c + 1):
                    x = count(i,j,k,l)
                    if x >= m:
                        ans += 1
    return ans

r,c,n,k = list(map(int,input().split()))

arr = [[0 for i in range(20)] for j in range(20)]

for i in range(n):
    x,y = list(map(int,input().split()))
    arr[x][y] = 1

print(solve(r,c,n,k))

