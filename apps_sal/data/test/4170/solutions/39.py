N = int(input())
h = list(map(int,input().split()))
memo = [0]*N
for i in range(1,N):
    if h[i]<=h[i-1]:
        memo[i] = memo[i-1] + 1 
print(max(memo))
