line = input().split()
h = int(line[0])
n = int(line[1])
last = 1
th = 2 ** h
ans = 1
l = 1
r = th
while th > 0:
    mid = (l + r) // 2
    if n <= mid:
        if last == 1:
            ans += 1
        else:
            ans += th
        last = 0
        r = mid
    else:
        if last == 0:
            ans += 1
        else:
            ans += th
        last = 1
        l = mid + 1
    th = th // 2
print(str(ans - 2))
