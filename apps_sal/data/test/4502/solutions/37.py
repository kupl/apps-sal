n = int(input())
a = list(map(int, input().split()))
o = [a[i] for i in range(2,n,2)]
e = [a[h] for h in range(1,n,2)]
if n%2 == 0:
    e.reverse()
    l = e + [a[0]] + o
    print(*l)
else:
    o.reverse()
    l = o + [a[0]] + e
    print(*l)
