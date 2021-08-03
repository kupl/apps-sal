x, y = map(int, input().split())
a = [y, y, y]
cnt = 0
while True:
    if a[0] == a[1] == a[2] == x:
        break
    if a[1] + a[2] > x:
        a[0] = x
    else:
        a[0] = a[1] + a[2] - 1
    cnt += 1
    a.sort()
print(cnt)
