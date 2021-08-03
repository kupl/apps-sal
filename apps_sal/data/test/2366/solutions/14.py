from collections import Counter

n = int(input())
al = list(map(int, input().split()))
c = Counter(al)

ans = 0
for k, v in c.items():
    ans += v * (v - 1) // 2

for a in al:
    b = c[a]
    print(ans - b * (b - 1) // 2 + (b - 1) * (b - 2) // 2)
