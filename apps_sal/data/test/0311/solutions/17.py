x, y, z, t1, t2, t3 = [int(x) for x in input().split()]

ld=abs(x-z)*t2 + t3*3 + t2*abs(x-y)
p = t1*abs(x-y)
if ld<=p:
        print("YES")
else:
        print("NO")

