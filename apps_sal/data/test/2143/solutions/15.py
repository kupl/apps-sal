n = int(input())
a = sorted(list(map(int, input().split())))
c = [0 for i in range(n)]
d = dict()
for i in range(n):
    for j in range(n):
        if i != j:
            s = a[i] + a[j]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

ans = 0
for i in list(d.values()):
    ans = max(ans, i)
print(ans // 2)
