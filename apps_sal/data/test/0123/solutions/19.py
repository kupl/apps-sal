(n, k) = map(int, input().split())
(a, b) = (list(map(int, input().split())), list(map(int, input().split())))
if k > 1:
    print('Yes')
else:
    a[a.index(0)] = b[0]
    if a == sorted(a):
        print('No')
    else:
        print('Yes')
