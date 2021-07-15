from collections import Counter
import itertools

n = int(input())
s = [input()[0] for _ in range(n)]

cnt = Counter(s)
ans = 0
for x, y, z in itertools.combinations("MARCH", 3):
    ans += cnt[x] * cnt[y] * cnt[z]
print(ans)
