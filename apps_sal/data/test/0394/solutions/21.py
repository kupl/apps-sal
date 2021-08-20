n = int(input())
a = [0] + list(map(int, input().split()))
dist = []
for i in range(1, n + 1):
    dist.append(a[i] - a[i - 1])
k_s = []
for k in range(1, n + 1):
    can = True
    for i in range(n):
        if dist[i] == dist[i % k]:
            pass
        else:
            can = False
            break
    if can:
        k_s.append(k)
print(len(k_s))
for t in k_s:
    print(t, end=' ')
