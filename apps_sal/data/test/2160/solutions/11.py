n, k = map(int, input().split())
x = list(map(int, input().split()))
d = {}
for i in range(k):
    d[x[i]] = i
ans = 0
v = [0] * n
for i in range(k):
    if v[x[i] - 1] == 0:
        if x[i] != 1:
            if d.get(x[i] - 1) == None or d.get(x[i] - 1) < i:
                ans += 1
        if x[i] != n:
            if d.get(x[i] + 1) == None or d.get(x[i] + 1) < i:
                ans += 1
        v[x[i] - 1] = 1
ans += 3 * (n - len(d))
if d.get(1) == None:
    ans -= 1
if d.get(n) == None:
    ans -= 1
print(ans)
