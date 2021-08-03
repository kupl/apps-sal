from collections import defaultdict
n = int(input())

d = defaultdict(int)
for i in range(1, n + 1):
    s = str(i)
    f = int(s[0])
    b = int(s[-1])
    d[(f, b)] += 1

ans = 0
for a in range(1, 10):
    for b in range(1, 10):
        ans += d[(a, b)] * d[(b, a)]
print(ans)
