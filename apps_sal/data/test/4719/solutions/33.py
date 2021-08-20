from collections import Counter
n = int(input())
S = [input() for _ in range(n)]
count = Counter(S[0])
for s in S[1:]:
    c = Counter(s)
    count = count & c
ls = sorted(count.items())
ans = ''
for (i, j) in ls:
    ans += i * j
print(ans)
