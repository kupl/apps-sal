from collections import defaultdict
n = int(input())
rec = defaultdict(list)
origi = list(map(int, input().split()))
for i in range(n):
    rec[origi[i]].append(i + 1)
a = sorted(origi, reverse=True)
l = 0
ans = []
for i in range(n):
    l += a[i] * i + 1
    ans.append(rec[a[i]].pop())
print(l)
for i in ans:
    print(i, end=' ')
print('')
