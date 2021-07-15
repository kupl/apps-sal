import sys
 
N, K = map(int, sys.stdin.readline().strip().split())
S = sys.stdin.readline().strip()
 
l = x = ans = 0
for r in range(N):
    if S[r] == '0' :
        if r == 0 or S[r-1] == '1':
            x += 1
    if x > K:
        while S[l] == '1':
            l += 1
        while S[l] == '0':
            l += 1
        x -= 1
    ans = max(ans, r-l+1)
print(ans)
