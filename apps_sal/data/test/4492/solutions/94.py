import math
N, x = list(map(int, input().split()))
L = [int(x) for x in input().split()]
ans = 0
for i in range(1,N):
    if L[i-1] + L[i] > x:
        if L[i-1] > x:
            ans += L[i-1] - x
            ans += L[i]
            L[i] = 0
        else:
            ans += L[i] + L[i-1] - x
            L[i] = x - L[i-1]
print(ans)

