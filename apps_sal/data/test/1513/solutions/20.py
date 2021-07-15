n,m,k = list(map(int,input().split()))
bi = list(map(int,input().split()))
ai = [0] * (n-1)
for i in range(n-1):
    ai[i] = bi[i+1] - bi[i]
ai.sort()
num = n - k
ans = k
for i in range(num):
    ans += ai[i]
print(ans)

