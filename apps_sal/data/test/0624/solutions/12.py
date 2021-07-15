n, k, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
sumi = sum(a)
ans = sumi / n
ct = 0
add = min(k * n, m - ct)
ans = max(ans, (sumi + add) / n)
for i in a:
    sumi -= i
    ct += 1
    n -= 1
    if ct > m or n == 0: break
    add = min(k * n, m - ct)
    ans = max(ans, (sumi + add) / n)
print(ans)
