x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

p.sort(reverse=True)
q.sort(reverse=True)

p2 = p[:x]
q2 = q[:y]

l = p2 + q2 + r
l.sort(reverse=True)

ans = sum(l[:x+y])
print(ans)
