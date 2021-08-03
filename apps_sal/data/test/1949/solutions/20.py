n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()
last = 0
i = 0
while k > 0:
    k -= 1
    f = True
    while f:
        if i == len(a):
            f = False
        elif a[i] > last:
            f = False
        else:
            i += 1
    if i == len(a):
        print(0)
    else:
        print(a[i] - last)
        last = a[i]
