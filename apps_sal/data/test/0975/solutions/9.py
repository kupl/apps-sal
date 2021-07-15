n = int(input())
a = sorted(map(int, input()))
b = sorted(map(int, input()))
was = [0] * n
cnt1 = cnt2 = 0
for i in range(n):
    mn = 10
    ind = -1
    for j in range(n):
        if not was[j] and a[j] <= b[i] < mn:
            mn = a[j]
            ind = j
    if ind != -1:
        was[ind] = 1
    else:
        cnt1 += 1
was = [0] * n
for i in range(n):
    mn = 10
    ind = -1
    for j in range(n):
        if not was[j] and a[j] < b[i] < mn:
            mn = a[j]
            ind = j
    if ind != -1:
        was[ind] = 1
        cnt2 += 1
print(cnt1)
print(cnt2)
