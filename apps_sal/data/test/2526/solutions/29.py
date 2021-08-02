X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

x = X - 1
y = Y - 1

p = sorted(p, reverse=True)
q = sorted(q, reverse=True)
r = sorted(r, reverse=True)

# print(p[:X],q[:Y])

if p[x] >= q[y]:
    a = q[y]
    f = 1
else:
    a = p[x]
    f = 2
while len(r) >= 1 and a < r[0]:
    #  print(a,r[0])
    if f == 1:
        #    print('f=1')
        q[y] = r[0]
        y -= 1
        r.pop(0)
    elif f == 2:
        #    print('f=2')
        p[x] = r[0]
        x -= 1
        r.pop(0)
    else:
        #    print('break1')
        break

#  print(x,y,p[x],q[y])

    if (y == -1 and x >= 0) or (x >= 0 and p[x] < q[y]):
        #    print('a=p[x]')
        a = p[x]
        f = 2
    elif (x == -1 and y >= 0) or (y >= 0 and p[x] >= q[y]):
        #    print('a=q[y]')
        a = q[y]
        f = 1
    else:
        #    print('break2')
        break

ans = 0
# print(p[:X],q[:Y])
for i in p[:X]:
    ans += i
for i in q[:Y]:
    ans += i

print(ans)
