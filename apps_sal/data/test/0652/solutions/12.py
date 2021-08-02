from collections import Counter
read = lambda: list(map(int, input().split()))
n = int(input())
p = [tuple(read()) for i in range(n)]
cnt = Counter()
for i in range(n):
    for j in range(i + 1, n):
        cnt[p[i][0] + p[j][0], p[i][1] + p[j][1]] += 1
ans = sum(i * (i - 1) // 2 for i in list(cnt.values()))
print(ans)
