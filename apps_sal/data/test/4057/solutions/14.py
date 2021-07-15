n=int(input())
a=[int(i) for i in input().split()]
p=set([])
for i in range(n):
    p.add(a.count(a[i]))
print(max(p))

