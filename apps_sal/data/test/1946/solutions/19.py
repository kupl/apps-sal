n = int(input())
d = dict()
for i in range(n):
    a, b = list(map(int, input().split()))
    try:
        d[a] = max(d[a], b)
    except:
        d.update({a: b})
m = int(input())
for i in range(m):
    a, b = list(map(int, input().split()))
    try:
        d[a] = max(d[a], b)
    except:
        d.update({a: b})
ans = 0
for i in d:
    ans += d[i]
print(ans)
