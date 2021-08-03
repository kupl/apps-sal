from sys import stdin, stdout


n, k = list(map(int, stdin.readline().rstrip().split()))
a = [int(x) for x in stdin.readline().rstrip().split()]
b = [int(x) for x in stdin.readline().rstrip().split()]

if k > 1:
    print('Yes')
else:
    zeroInd = a.index(0)
    a[zeroInd] = b[0]
    aSort = sorted(a)
    identical = True
    for i in range(n):
        if aSort[i] != a[i]:
            identical = False
    if identical:
        print('No')
    else:
        print('Yes')
