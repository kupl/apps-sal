from collections import Counter

n, k = map(int, input().split())

d = Counter()
for _ in range(n):
    a, b = map(int, input().split())
    d[a] += b

x = sorted(d.items(), key=lambda x: x[0])
cnt = 0
for a, b in x:
    cnt += b
    if cnt >= k:
        print(a)
        return
