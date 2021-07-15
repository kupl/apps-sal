n, L, a = [int(i) for i in input().split()]
x = 0

prevl = 0
for i in range(n):
    t, l = [int(i) for i in input().split()]
    if t-prevl>=a:
        x+=(t-prevl)//a
    prevl = t+l
x+=(L-prevl)//a

print(x)

