(n, k) = [int(x) for x in input().split()]
l1 = [int(x) - 1 for x in input().split()]
l2 = [0 for x in range(0, n)]
l3 = [0 for x in range(0, n)]
l4 = [[] for x in range(0, n)]
for i in range(0, n):
    l4[i].append(i - 1)
    l4[i].append(i + 1)
for i in range(0, n):
    l3[l1[i]] = i
i = n - 1
x = 1
while i >= 0:
    t = l3[i]
    if l2[t] != 0:
        i -= 1
        continue
    else:
        l2[t] = x
        j = 1
        m = l4[t][1]
        while j <= k and m < n:
            if l2[m] != 0:
                if l4[m][1] > n - 1:
                    break
                m = l4[m][1]
                continue
            l2[m] = x
            if l4[m][1] > n - 1:
                break
            m = l4[m][1]
            j += 1
        a = m
        j = 1
        m = l4[t][0]
        while j <= k and m > -1:
            if l2[m] != 0:
                if l4[m][0] < 0:
                    break
                m = l4[m][0]
                continue
            l2[m] = x
            if l4[m][0] < 0:
                break
            m = l4[m][0]
            j += 1
        b = m
        if a < n:
            l4[a][0] = b
        if b > -1:
            l4[b][1] = a
    if x == 1:
        x = 2
    else:
        x = 1
    i -= 1
for element in l2:
    print(element, end='')
