from collections import Counter
N = int(input())
S = [Counter(input()) for _ in range(N)]
x = S[0]
for i in range(1, N):
    x = x & S[i]
ans = []
for (k, v) in x.items():
    for i in range(v):
        ans.append(k)
ans = sorted(ans)
print(''.join(ans))
