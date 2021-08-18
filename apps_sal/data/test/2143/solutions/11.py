n = int(input())
l = list(map(int, input().split()))
d = {}
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        d.setdefault(l[i] + l[j], 0)
        d[l[i] + l[j]] += 1
print(sorted(d.values())[-1] // 2)
