n = int(input())
w = list(map(int,input().split()))
sumw = [0]*(n+1)
for i in range(n):
    sumw[i+1] += (sumw[i] + w[i])
ans = 10**9
for i in range(n):
    ans = min(ans,abs(sumw[n]-2*sumw[i+1]))
print(ans)
