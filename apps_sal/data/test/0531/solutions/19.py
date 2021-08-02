n = int(input())
a = list(map(int, input().split()))
a.sort()
sr = sum(a) / n
x = []
min1 = min(a)
max1 = max(a)
targ = False
if min1 + 2 != max1:
    print(n)
    print(*a)
    min1 = int(sr) - 1
    max1 = int(sr) + 1
else:
    sred = (min1 + max1) // 2
    i = 0
    k = 0
    u = [0, 0, 0]
    for j in a:
        if j == min1:
            u[0] += 1
        elif j == max1:
            u[1] += 1
        else:
            u[2] += 1
    if (min(u[0], u[1]) * 2 > u[2]):
        while min1 == a[k] and max1 == a[-1 - k]:
            x += [sred, sred]
            a[k] = -200001
            a[-1 - k] = -200001
            i += 2
            k += 1
        print(n - i)
        for j in a:
            if j != -200001:
                x += [j]
        print(*x)
    else:
        k = u[2] - u[2] % 2
        while u[2] > 1:
            u[2] -= 2
            x += [min1, max1]
        if u[2] > 0:
            x += [sred]
        print(n - k)
        for i in range(u[0]):
            x += [min1]
        for i in range(u[1]):
            x += [max1]
        print(*x)
