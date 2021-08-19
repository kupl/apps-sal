import sys
input = sys.stdin.readline
N = int(input())
S = list(input().strip())
ans = 0
for i in range(N):
    ans = max(ans, len(set(S[:i]) & set(S[i:])))
print(ans)
