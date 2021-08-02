from collections import Counter
n = int(input())
lst = []
for _ in range(n):
    s = sorted(list(input()))
    lst.append("".join(s))
c = Counter(lst)
ans = 0
for k, v in c.items():
    ans += v * (v - 1) // 2

print(ans)
