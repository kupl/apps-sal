from collections import Counter
n = int(input())
a = []
ans = 0
for i in range(n):
    b = sorted(input())
    b = ''.join(b)
    a.append(b)
mycounter = Counter(a)
for j in mycounter.values():
    l = j
    if l >= 2:
        ans += (l - 1 + 1) * (l - 1) // 2
print(ans)
