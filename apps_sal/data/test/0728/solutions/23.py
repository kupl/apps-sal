n = int(input())
a = list(map(int, input().split()))
i = -1
k = 0
lim = a[0]
a[0] = 0
a = sorted(a)
n -= 1
while lim <= a[-1]:
    while lim <= a[-1] and a[-1] >= a[-2]:
        lim += 1
        a[-1] -= 1
        k += 1
    while i > -n and a[i] < a[i - 1]:
        a[i], a[i - 1], i = a[i - 1], a[i], i - 1
    i = -1
print(k)
