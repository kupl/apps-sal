(n, k) = map(int, input().split())
(rp, sp, pp) = map(int, input().split())
p = {'r': pp, 's': rp, 'p': sp}
t = [s for s in input()]
ans = 0
for i in range(n):
    if i >= k and t[i] == t[i - k]:
        t[i] = '.'
        continue
    ans += p[t[i]]
print(ans)
