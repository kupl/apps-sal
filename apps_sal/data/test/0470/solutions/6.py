from collections import Counter

t = Counter(list(map(int, input().split())))
s = ans = sum(x * t[x] for x in t)
for x in t:
    if t[x] > 1:
        ans = min(ans, s - x * min(3, t[x]))
print(ans)
