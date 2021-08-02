a = [int(i)for i in input().split()]
b = range(a[2] + 1)
c = b[0::a[1]]
c = [i - a[0] for i in c]
c = [i for i in c if i > 0]
if c == []: print(-1)
else: print(' '.join([str(i)for i in c]))
