(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
if x == 0:
    print(sum(a))
else:
    eat = 0
    for i in range(n - 1):
        tmp = 0
        if a[i] + a[i + 1] > x:
            tmp = a[i] + a[i + 1] - x
            eat += tmp
            if tmp > a[i + 1]:
                tmp -= a[i + 1]
                a[i + 1] = 0
                a[i] -= tmp
            else:
                a[i + 1] -= tmp
    print(eat)
