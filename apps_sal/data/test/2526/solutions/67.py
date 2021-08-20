(x, y, a, b, c) = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]
p.sort()
q.sort()
r.sort()
p = p[-x:]
q = q[-y:]
ans = p + q + r
ans.sort()
ans = ans[-x - y:]
print(sum(ans))
