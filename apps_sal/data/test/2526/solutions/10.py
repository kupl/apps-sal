(x, y, a, b, c) = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
s = p[:x] + q[:y]
s.sort()
ans = sum(s)
for (si, ri) in zip(s, r):
    if si < ri:
        ans += ri - si
print(ans)
