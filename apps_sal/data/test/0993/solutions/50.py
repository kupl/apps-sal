(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = 0
d = {0: 1}
for i in a:
    s = (s + i) % m
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
ans = 0
for (k, v) in list(d.items()):
    ans += v * (v - 1) // 2
print(ans)
