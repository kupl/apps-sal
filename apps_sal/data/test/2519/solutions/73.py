n, k = map(int,input().split())
p = list(map(lambda x:int(x)+1,input().split()))

s = [0]*(n+1)

for i in range(n):
    s[i+1] = s[i] + p[i]
    
res = 0
for i in range(n-k+1):
    res = max(res,s[i+k]-s[i])
print(res/2)
