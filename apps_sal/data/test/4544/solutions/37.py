from collections import Counter
n = int(input())
a = list(map(int, input().split()))

p = []
for i in range(n):
    p.append(a[i] - 1)
    p.append(a[i])
    p.append(a[i] + 1)


c = Counter(p).most_common()

m = list(c)[0][0]

ans = 0

for i in range(n):
    if abs(a[i] - m) <= 1:
        ans += 1

print(ans)
