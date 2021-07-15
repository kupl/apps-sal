a, b = map(int, input().split())
c = [-b-1]
for i in range(a):
    k, l = map(int, input().split())
    c.append(k*60+l)
c.append(10000000000000000)
for i in range(a+1):
    if c[i+1]-c[i]> 2*b+1:
        u = c[i]+b+1
        print(u//60, u%60)
        break
