n = int(input())
lst = [int(x) for x in input().split()]
a = []
for x in range(len(lst) - 1):
    a.append(lst[x + 1] - lst[x])
if len(a) == 0:
    print(0)
else:
    mini = min(a)
    maxi = max(a)
    if maxi - mini > 4:
        print(-1)
    else:
        m1 = (maxi + mini) // 2
        m2 = (maxi + mini + 1) // 2
        ar = []
        k = 0
        flag = True
        for x in range(1, n):
            if lst[0] + m1 * x != lst[x] and lst[x] - 1 <= lst[0] + m1 * x <= lst[x] + 1:
                k += 1
            else:
                if lst[0] + m1 * x == lst[x]:
                    continue
                flag = False
                break
        if flag:
            ar.append(k)
        k = 0
        flag = True
        for x in range(1, n):
            if lst[0] + m2 * x != lst[x] and lst[x] - 1 <= lst[0] + m2 * x <= lst[x] + 1:
                k += 1
            else:
                if lst[0] + m2 * x == lst[x]:
                    continue
                flag = False
                break
        if flag:
            ar.append(k)
        k = 1
        flag = True
        lst[0] -= 1
        for x in range(1, n):
            if lst[0] + m1 * x != lst[x] and lst[x] - 1 <= lst[0] + m1 * x <= lst[x] + 1:
                k += 1
            else:
                if lst[0] + m1 * x == lst[x]:
                    continue
                flag = False
                break
        if flag:
            ar.append(k)
        k = 1
        flag = True
        for x in range(1, n):
            if lst[0] + m2 * x != lst[x] and lst[x] - 1 <= lst[0] + m2 * x <= lst[x] + 1:
                k += 1
            else:
                if lst[0] + m2 * x == lst[x]:
                    continue
                flag = False
                break
        if flag:
            ar.append(k)
        k = 1
        lst[0] += 2
        flag = True
        for x in range(1, n):
            if lst[0] + m1 * x != lst[x] and lst[x] - 1 <= lst[0] + m1 * x <= lst[x] + 1:
                k += 1
            else:
                if lst[0] + m1 * x == lst[x]:
                    continue
                flag = False
                break
        if flag:
            ar.append(k)
        k = 1
        flag = True
        for x in range(1, n):
            if lst[0] + m2 * x != lst[x] and lst[x] - 1 <= lst[0] + m2 * x <= lst[x] + 1:
                k += 1
            else:
                if lst[0] + m2 * x == lst[x]:
                    continue
                flag = False
                break
        if flag:
            ar.append(k)
        if len(ar) != 0:
            print(min(ar))
        else:
            print(-1)
