n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] % 2 == 0:
        a[i] = 0
    else:
        a[i] = 1
k = a.count(1)
if k % 2 == 1:
    print('First')
else:
    if k == 0:
        print('Second')
    else:
        print('First')
