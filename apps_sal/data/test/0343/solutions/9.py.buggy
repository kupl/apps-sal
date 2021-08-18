n, k, p, x, y = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

if n == 1:
    if y > x:
        print(-1)
    else:
        print(y)
    return

a.sort()
med_pos = n // 2
s = sum(a)
if (len(a) > med_pos) and (a[med_pos] < y):
    print(-1)
    return

if s + (n - k) > x:
    print(-1)
    return

ind = -1
for i in range(len(a)):
    if a[i] >= y:
        ind = i
        break

if ind == -1:
    ind = len(a)

left = min(n - k, med_pos - ind)
right = max(0, n - k - left)

if s + left + y * right > x:
    print(-1)
    return

for i in range(left):
    print(1, end=' ')
for i in range(right):
    print(y, end=' ')
