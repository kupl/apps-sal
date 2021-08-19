from collections import Counter
(n, m) = list(map(int, input().split()))
l = [Counter() for i in range(m)]
for i in range(n):
    a = input()
    for (c, d) in zip(a, l):
        d[c] += 1
ans = 0
for (p, d) in zip(list(map(int, input().split())), l):
    ans += p * max(d.values())
print(ans)
