import sys

input = sys.stdin.readline
N, K = map(int, input().split())
S = list(input().strip())

ans = 0
split = 0
pre = S[0]
for i in range(1, N):
    if pre == S[i]:
        ans += 1
    else:
        split += 1
    pre = S[i]

# print(ans, split)
print(ans + min(2*K, split))
