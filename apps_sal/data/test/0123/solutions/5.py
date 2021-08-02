n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if k == 1:
    ind = a.index(0)
    a[ind] = b[0]
    st = False
    for i in range(n - 1):
        if a[i] >= a[i + 1]:
            st = True
            break
    if st:
        print('Yes')
    else:
        print('No')
else:
    print('Yes')
