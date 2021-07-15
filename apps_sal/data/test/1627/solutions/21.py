n = int(input())
a = [int(s) for s in input().split()]
for j in range(n):
    k = 0
    i = 0
    while i < n-1:
        if a[i] > a[i+1]:
            k += 1
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
            print(i+1, i+2)
        i += 2
    i = 1
    while i < n-1:
        if a[i] > a[i+1]:
            k += 1
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
            print(i+1, i+2)
        i += 2
    if k == 0:
        break

