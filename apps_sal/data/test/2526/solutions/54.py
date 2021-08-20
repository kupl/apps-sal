(x, y, a, b, c) = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p = sorted(p, reverse=True)
q = sorted(q, reverse=True)
pq = sorted(p[:x] + q[:y])
r = sorted(r)
ans = 0
j = r.pop()
for i in pq:
    if i < j:
        ans += j
        j = 0
        if r:
            j = r.pop()
    else:
        ans += i
print(ans)
