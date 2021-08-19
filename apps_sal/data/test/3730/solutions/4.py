n = int(input())
alist = [int(x) for x in input().split()]
maximum = 2
l = [1] * n
r = l[:]
if n < 3:
    print(n)
    quit()
for i in range(0, n - 1):
    if alist[i] < alist[i + 1]:
        l[i + 1] += l[i]
    if alist[n - 1 - i] > alist[n - 2 - i]:
        r[n - 2 - i] += r[n - 1 - i]
for i in range(1, n - 1):
    if alist[i - 1] + 1 < alist[i + 1]:
        maximum = max(maximum, l[i - 1] + r[i + 1] + 1)
    else:
        maximum = max(maximum, l[i - 1] + 1, r[i + 1] + 1)
maximum = max(maximum, r[1] + 1, l[n - 2] + 1)
print(maximum)
