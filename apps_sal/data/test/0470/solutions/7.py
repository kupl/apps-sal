read = lambda: list(map(int, input().split()))
t = sorted(read())
Sum = ans = sum(t)
a = set(t)
for i in a:
    if t.count(i) == 1: continue
    cur = Sum - min(3, t.count(i)) * i
    ans = min(ans, cur)
print(ans)

