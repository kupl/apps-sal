###########コーディング
a, b, c, x, y = map(int,input().split())

n = a*x+b*y
m = c * 2 * max(x,y)
p = a if x>y else b
l = c*2*min(x,y)+p*abs(x-y)
ans = min(n,min(m,l))

print(ans)
