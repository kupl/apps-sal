from collections import Counter

n = int(input())
l = list(map(int, input().split()))

ans = 0
s = 0

for i, a in enumerate(l):
    ans += a * i - s
    s += a

c = Counter()
for a in l:
    ans -= c[a-1]
    ans += c[a+1]
    c[a] += 1

print(ans)
