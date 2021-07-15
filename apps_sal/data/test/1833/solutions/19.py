n = int(input())
A = [int(i) for i in input().split()]

def fct(x):
    ans = []
    for i in range(1, x+1):
        if i*i>x:
            break
        if x%i==0:
            ans.append(i)
            if i*i!=x:
                ans.append(x//i)
    return sorted(ans)[::-1]

dp = [0 for i in range(10**6 + 5)]

mod = 10**9 + 7

dp[0] = 1
for i in A:
    do = fct(i)
    for j in do:
        dp[j] = (dp[j]+dp[j-1])%mod

c = 0
for i in dp:
    c+=i
    if c>=mod:
        c-=mod
        
print((c-1)%mod)

