se = set()
n = int(input())
cf = {}
for i in range(n):
    a,x = [int(s) for s in input().split()]
    cf[a] = x
    se.add(a)
m = int(input())
tc = {}
for i in range(m):
    b,y = [int(s) for s in input().split()]
    tc[b] = y
    se.add(b)

sum = 0
for e in se:
    sum += max(cf.get(e, 0), tc.get(e, 0))

print(sum)
