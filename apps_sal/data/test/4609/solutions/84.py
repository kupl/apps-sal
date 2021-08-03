from collections import Counter

n = int(input())
al = list(int(input()) for _ in range(n))
c = Counter(al)
ans = 0
for k, v in c.items():
    if v % 2 != 0:
        ans += 1

print(ans)
