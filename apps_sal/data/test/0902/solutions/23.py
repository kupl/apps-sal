n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
maxa = max(a)
if len(a) <= k:
    print(maxa)
else:
    qq = a[0]
    j = 0
    for i in range(1, len(a)):
        if j == k:
            print(qq)
            break
        if a[i] == maxa:
            print(maxa)
            break
        if a[i] > qq:
            qq = a[i]
            j = 1
        else:
            j += 1

