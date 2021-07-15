n, m = [int(i) for i in input().split()]
s1 = []
s2 = []
if n > m:
    print("YES")
elif m > n:
    print("NO")
else:
    r = set()
    for i in range(n):
        s1.append(input())
        r.add(s1[-1])
    for i in range(m):
        s2.append(input())
        r.add(s2[-1])
    t = len(s2)+len(s1)-len(r)
    if t%2 == 1:
        print("YES")
    else:
        print("NO")


