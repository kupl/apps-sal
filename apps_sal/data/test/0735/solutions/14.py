n = int(input())
a = list(map(int, input().split()))


def Reverse(a, l, r):
    (i, j) = (l, r)
    while i < j:
        (a[i], a[j]) = (a[j], a[i])
        i += 1
        j -= 1


def IsSorted(a):
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return False
    return True


for l in range(n - 1):
    if a[l] > a[l + 1]:
        r = l + 1
        while r + 1 < n and a[r] > a[r + 1]:
            r += 1
        Reverse(a, l, r)
        if IsSorted(a):
            print('yes')
            print(l + 1, r + 1)
        else:
            print('no')
        break
else:
    print('yes')
    print(1, 1)
