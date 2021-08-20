a = input().split()
a = [int(i) for i in a]
if sum(a[:2]) >= a[2]:
    print('Yes')
else:
    print('No')
