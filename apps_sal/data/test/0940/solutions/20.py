a = list([int(s) for s in str(input()).strip().split(' ', 2)])
cnt = 0
a = sorted(a)
while a[0] + a[1] <= a[2]:
    a[1] += 1
    cnt += 1
print(cnt)
