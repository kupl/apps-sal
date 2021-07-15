#https://codeforces.com/contest/1203/problem/F2 

n, r = list(map(int, input().split()))
arr  = [list(map(int, input().split())) for _ in range(n)] 

def solve1(cur, arr):
    cnt=0

    while len(arr) > 0:
        max_inc = -9999
        choose  = None 
        for a, b in arr:
            if cur >= a and max_inc < b:
                max_inc = b
                choose  = a
                
        if choose is None:
            flg=False
            break
        
        cnt+=1
        cur+=max_inc
        arr.remove([choose, max_inc])

    return cur, cnt

arr1 = [[x, y] for x, y in arr if y >= 0]
arr2 = [[x, y] for x, y in arr if y <  0]

r, cnt = solve1(r, arr1) 
n      = len(arr2) 
arr2   = [[]] + sorted(arr2, key=lambda x:x[0]+x[1], reverse=True) 
dp     = [[-1] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = r
    
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] = dp[i-1][j]
        if dp[i-1][j-1] >= arr2[i][0] and dp[i-1][j-1] + arr2[i][1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+arr2[i][1])
            
ans = 0            
for j in range(n+1):
    if dp[n][j] >= 0:
        ans = j

print(ans+cnt)        

#3 4
#4 6
#10 -2
#8 -1

