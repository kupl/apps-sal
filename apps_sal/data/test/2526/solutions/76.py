(x, y, a, b, c) = map(int, input().split())
p = [int(x) for x in input().rstrip().split()]
q = [int(x) for x in input().rstrip().split()]
r = [int(x) for x in input().rstrip().split()]
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
p = p[:x]
q = q[:y]
pq = p + q
pqr = pq + r
pqr.sort(reverse=True)
print(sum(pqr[:x + y]))
