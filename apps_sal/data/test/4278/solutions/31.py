n = int(input())
d = {}
ans = 0
for i in range(n):
    s = ''.join(sorted(input()))
    if s in d:
        ans += d[s]
        d[s] += 1
    else:
        d[s] = 1
print(ans)
