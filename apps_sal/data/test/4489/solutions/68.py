from collections import Counter
N = int(input())
S = [''.join(sorted(input())) for _ in range(N)]
M = int(input())
T = [''.join(sorted(input())) for _ in range(M)]

s = Counter(S)
t = Counter(T)

ans = 0
for k, v in list(s.items()):
    tmp = v
    tmp -= t[k]
    ans = max(ans, tmp)
print(ans)
