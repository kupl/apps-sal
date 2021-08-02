n = int(input())
a = list(str(n))
s = sum([int(a[i]) for i in range(len(a))])
if n % s == 0:
    print('Yes')
else:
    print('No')
