a = input().split()
lozung = input()
n = int(a[0])
k = int(a[1])
tol = k - 1
tor = n - k
if tol > tor:
    for i in range(tor):
        print('RIGHT')
    for i in range(1, n):
        print('PRINT ' + lozung[n - i])
        print('LEFT')
    print('PRINT ' + lozung[0])
else:
    for i in range(tol):
        print('LEFT')
    for i in range(n - 1):
        print('PRINT ' + lozung[i])
        print('RIGHT')
    print('PRINT ' + lozung[n - 1])
