import itertools

a = list(map(int, input().split()))
total = sum(a)
if total % 2 != 0:
    print('No')
    return

p = list(itertools.product([0, 1], repeat=4))
for i in range(len(p)):
    if a[0]*p[i][0] + a[1]*p[i][1] + a[2]*p[i][2] + a[3]*p[i][3] == total // 2:
        print('Yes')
        return
print('No')

