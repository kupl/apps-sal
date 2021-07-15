from collections import deque

def ans(n,k,a):
    dp = [0 for i in range(n+1)]
    q = deque()
    for i in range(1,n+1):
        r = None
        while len(q) > 0:
            cur = q[0]
            if i <= cur+k:
                r = cur
                break
            q.popleft()
        if a[i-1]=='0':
            if r != None:
                dp[i] = min(r+dp[max(0,r-k-1)],r+dp[r-1])
            else:
                dp[i] = i+dp[i-1]
        else:
            q.append(i)
            if r!=None:
                dp[i] = min(i+dp[max(0,i-k-1)],r+dp[max(0,r-k-1)],r+dp[r-1])
            else:
                dp[i] = min(i+dp[max(0,i-k-1)],i+dp[i-1])
    return dp[n]    


n,k = list(map(int,input().split(" ")))
a = input()
out = ans(n,k,a)
print(out)  
