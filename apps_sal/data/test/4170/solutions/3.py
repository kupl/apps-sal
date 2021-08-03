n = int(input())
h = list(map(int, input().split()))
count = 0
lst = []
if (n == 1):
    print((0))
else:
    for i in range(n - 1):
        if (h[i] >= h[i + 1]):
            count = count + 1
        else:
            lst.append(count)
            count = 0
    if (count != 0):
        lst.append(count)

    lst.sort()
    lst.reverse()

    print((lst[0]))
