import sys
read = sys.stdin.readline
(n, k) = list(map(int, read().split()))
sushi = [[] for _ in range(n)]
for i in range(n):
    (t, d) = list(map(int, read().split()))
    t -= 1
    sushi[t].append(d)
max_sushi = []
other_sushi = []
for i in range(n):
    if len(sushi[i]) == 0:
        continue
    sushi[i].sort()
    max_sushi.append(sushi[i][-1])
    for j in range(len(sushi[i]) - 1):
        other_sushi.append(sushi[i][j])
max_sushi.sort(reverse=True)
other_sushi.sort(reverse=True)
for i in range(len(max_sushi) - 1):
    max_sushi[i + 1] += max_sushi[i]
for i in range(len(other_sushi) - 1):
    other_sushi[i + 1] += other_sushi[i]
a = len(max_sushi)
b = len(other_sushi)
ans = 0
for x in range(1, k + 1):
    if x > a or k - x > b:
        continue
    other = 0 if k - x - 1 < 0 else other_sushi[k - x - 1]
    ans = max(ans, x * x + max_sushi[x - 1] + other)
print(ans)
