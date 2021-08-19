from collections import Counter
n = int(input())
S = [input() for _ in range(n)]
ans = Counter(S[0])
for s in S[1:]:
    ans = ans & Counter(s)
print(''.join(sorted([k * v for (k, v) in ans.items()])))
