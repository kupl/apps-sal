n, k = map(int, input().split())
r, s, p = map(int, input().split())
d = {'r': p, 's': r, 'p': s}
t = input()
ans = 0
for i in range(k):
    x = t[i]
    ans += d[x]
    for j in range(i + k, n, k):
        if t[j] != x:
            x = t[j]
            ans += d[x]
        else:
            x = 'z'
print(ans)
