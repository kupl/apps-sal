q = int(input())
for i in range(q):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    first = a[0]
    second = -1
    third = -1
    maxa = a[0]
    arr = []
    for i in range(n):
        if first % a[i] != 0:
            if second == -1:
                second = a[i]
            elif second % a[i] != 0:
                if third == -1:
                    third = a[i]
                else:
                    break
    if maxa % 30 == 0:
        if maxa // 2 in a and maxa // 3 in a and (maxa // 5 in a):
            print(max(first + max(second, 0) + max(third, 0), maxa // 2 + maxa // 3 + maxa // 5))
        else:
            print(max(first, 0) + max(second, 0) + max(third, 0))
    else:
        print(max(first, 0) + max(second, 0) + max(third, 0))
