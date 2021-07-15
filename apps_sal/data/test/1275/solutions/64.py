import bisect

N, K = map(int,input().split())

ans = 0

for i in range(2,2*N+1):
    if 2 <= i - K <= 2*N:
        ans = min((i-K) - 1, 2*N - (i-K) + 1) * min(i - 1, 2*N - i + 1) + ans
        
print(ans)
