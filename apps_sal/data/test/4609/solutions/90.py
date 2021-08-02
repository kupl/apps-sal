from collections import Counter
n = int(input())
a = Counter([input() for _ in range(n)])
ans = 0
for x in a.values():
    if x % 2 != 0:
        ans += 1
print(ans)
