def iscontained(a,b):
    l = max(a[0],b[0])
    r = min(a[1],b[1])
    return (l < r, (l,r))

def solve(p,v,n):
    iter = 0
    l = 0.0
    r = 1000000010.0
    tupl = [0] * 60001
    while(iter < 60):
        flag = True
        m = (l + r)/2
        intersect = (p[0] - v[0] * m,p[0] + v[0]* m)
        for i in range(1,n):
            tupl[i] = (p[i] - v[i] * m,p[i] + v[i]*m)
            lap,intersect = iscontained(intersect,tupl[i])
            if not lap:
                flag = False
                break
        if not flag:
            l = m
        else:
            r = m
        iter = iter+1
    # print(l,r)
    print("%.9f" % l)

n = int(input())
pos = list()
vel = list()
for i in map(float,input().split()):
    pos.append(i)
for i in map(float,input().split()):
    vel.append(i)

solve(pos,vel,n)
