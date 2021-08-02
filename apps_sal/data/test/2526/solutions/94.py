x, y, a, b, c = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)
pq = sorted(p[:x] + q[:y])
ans = sum(pq)
i = 0
while i < min(a + b, c):
    if r[i] <= pq[i]:
        break
    ans += r[i] - pq[i]
    i += 1
print(ans)
