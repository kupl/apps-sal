from collections import defaultdict

dd = defaultdict(int)
n = int(input())
ans = 0
for _ in range(n):
    m = list(input())
    m.sort()
    tmp = "".join(m)
    ans += dd[tmp]
    dd[tmp] += 1
print(ans)
