def count(a, x):
    ans = 0
    for y in a:
        if x == y:
            ans += 1
    return ans


a = list(map(int, input().split()))
s = sum(a)
ans = s
for x in a:
    v = count(a, x)
    if 2 <= v:
        ans = min(ans, s - min(v, 3) * x)
print(ans)
