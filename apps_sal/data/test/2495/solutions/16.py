n = int(input())
a = list(map(int, input().split()))
b = a[:]
(cnt1, cnt2) = (0, 0)
s = 0
for i in range(n):
    if i % 2 == 0 and s + a[i] <= 0 or (i % 2 == 1 and s + a[i] >= 0):
        cnt1 += abs(s + a[i]) + 1
        if i % 2:
            s = -1
        else:
            s = 1
    else:
        s += a[i]
s = 0
for i in range(n):
    if i % 2 == 1 and s + a[i] <= 0 or (i % 2 == 0 and s + a[i] >= 0):
        cnt2 += abs(s + a[i]) + 1
        if i % 2:
            s = 1
        else:
            s = -1
    else:
        s += a[i]
print(min(cnt1, cnt2))
