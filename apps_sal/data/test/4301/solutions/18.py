n = int(input())
a = [int(input()) for i in range(n)]
b = a[:]
p = max(a)
b.remove(p)
q = max(b)
for i in a:
    if i != p:
        print(p)
    else:
        print(q)
