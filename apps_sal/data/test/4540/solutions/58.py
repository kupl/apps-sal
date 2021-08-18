n = int(input())
a = list(map(int, input().split()))

sm_al = abs(a[0]) + abs(a[n - 1])
for i in range(n - 1):
    sm_al += abs(a[i + 1] - a[i])

sm1 = sm_al - abs(a[1] - a[0]) - abs(a[0]) + abs(a[1])
print(sm1)
for i in range(1, n - 1):
    sm = sm_al - abs(a[i + 1] - a[i]) - abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i - 1])
    print(sm)
smn = sm_al - abs(a[n - 1] - a[n - 2]) - abs(a[n - 1]) + abs(a[n - 2])
print(smn)
