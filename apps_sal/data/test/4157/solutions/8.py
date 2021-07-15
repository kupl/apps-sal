n = int(input())
a = list(map(int, input().split()))
l = [a[0]]
for i in range(1, n):
    for j in range(i, n):
        if l[-1] * 2 == a[j]:
            l += [a[j]]
            a[i], a[j] = a[j], a[i]
            break
        if (l[-1] // 3 == a[j]) and (l[-1] % 3 == 0):
            l += [a[j]]
            a[i], a[j] = a[j], a[i]
            break
        if l[0] * 3 == a[j]:
            l = [a[j]] + l
            a[i], a[j] = a[j], a[i]
            break
        if (l[0] // 2 == a[j]) and (l[0] % 2 == 0):
            l = [a[j]] + l
            a[i], a[j] = a[j], a[i]
            break
print(*l)
