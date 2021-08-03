n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
maxa = max(a)
if len(a) <= k:
    print(maxa)
else:
    curr = a[0]
    j = 0
    for i in range(1, len(a)):
        if j == k:
            print(curr)
            break
        if a[i] == maxa:
            print(maxa)
            break
        if a[i] > curr:
            curr = a[i]
            j = 1
        else:
            j += 1
