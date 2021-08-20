a = input().split()
a = [int(j) for j in a]
a.append(a[:2])
a.append(a[2:4])
if sum(a[4]) > sum(a[5]):
    print('Left')
if sum(a[4]) == sum(a[5]):
    print('Balanced')
if sum(a[4]) < sum(a[5]):
    print('Right')
