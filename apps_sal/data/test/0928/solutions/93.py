from itertools import accumulate
import bisect
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
Asum = [0]+list(accumulate(A))
ans = 0
for i in range(1, N+1):
    ind = bisect.bisect_left(Asum, Asum[i-1]+K)
    ans += N-ind+1
print(ans)

