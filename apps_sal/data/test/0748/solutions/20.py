n = int(input())
a = list(map(int,input().split()))
c = [0]*8
for i in a:
    c[i]+=1
if c[5] or c[7]:
    print(-1)
    return
t1 = c[3]
c[3] = 0
c[1] -= t1
c[6] -= t1
t2 = c[6]
c[1] -= t2
c[6] = 0
c[2] -= t2
t3 = c[4]
c[4] = 0
c[2] -= t3
c[1] -= t3
if c.count(0) != 8 or t1<0 or t2<0 or t3<0:
    print(-1)
else:
    for i in range(t1):
        print('1 3 6')
    for i in range(t2):
        print('1 2 6')
    for i in range(t3):
        print('1 2 4')
