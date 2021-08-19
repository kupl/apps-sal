(n, m, k) = list(map(int, input().split()))
power = list(map(int, input().split()))
sch = list(map(int, input().split()))
chosen = list(map(int, input().split()))
ans = 0
d = dict()
for i in range(n + 1):
    d[i] = []
for i in range(n):
    d[sch[i]].append((power[i], i + 1))
for i in range(n + 1):
    d[i] = sorted(d[i])
for i in range(k):
    if d[sch[chosen[i] - 1]][-1][1] != chosen[i]:
        ans += 1
print(ans)
