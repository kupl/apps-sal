n, m = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
# print(a)
Min = a[n - 1] - a[0]
# print(Min)
for i in range(m - n + 1):
    x = a[i + n - 1] - a[i]
#	print('x=',x)
#	print(i,i+n-1)
    if x < Min:
        Min = x
print(Min)
