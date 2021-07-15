from collections import Counter
from sys import stdin
def input():
    return stdin.readline().strip()

n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

s = Counter(s)
t = Counter(t)

ans = 0
for key, num in s.items():
    if key in t:
        if ans < num - t[key]:
            ans = num - t[key]
    else:
        if ans < num:
            ans = num

print(ans)
