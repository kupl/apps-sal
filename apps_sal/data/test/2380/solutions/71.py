n, m = map(int, input().split())
l = [(a, 1) for a in list(map(int, input().split()))]
for i in range(m):
    b, c = map(int, input().split())
    l.append((c, b))
l = sorted(l)[::-1]
ans = 0

for i, j in l:
    if j < n:
        ans += i*j
        n -= j
    else:
        ans += n*i
        break

print(ans)
