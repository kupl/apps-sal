(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = sum(a)
a.sort()
lastlevel = 0
level = 0
got = 0
for i in a:
    got = max(got, i)
    level = min(level + 1, got)
    if i > 0:
        ans -= 1
        lastlevel = level
ans -= got - level
print(ans)
