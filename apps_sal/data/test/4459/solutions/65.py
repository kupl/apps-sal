n = int(input())
A = list(map(int, input().split()))

d = {}
for a in A:
    d[a] = d.get(a, 0) + 1

ans = 0
for a in d:
    if d[a]>a:
        ans += d[a]-a
    elif d[a]<a:
        ans += d[a]
print(ans)
