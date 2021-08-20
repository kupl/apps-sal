input()
a = [int(i) for i in input().split()]
b = [sum(a[::3]), sum(a[1::3]), sum(a[2::3])]
c = ['chest', 'biceps', 'back']
print(c[b.index(max(b))])
