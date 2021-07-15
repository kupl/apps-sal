n, mm = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
for i in range(mm):
    b[i] = [b[i], i]
b.sort()
ans = ['0' for i in range(mm)]
last = -1
for i in b:
    l = last
    r = n
    while r - l > 1:
        m = (r + l) // 2
        if a[m] <= i[0]:
            l = m
        else:
            r = m
    last = l
    ans[i[1]] = str(l + 1)
print(' '.join(ans))

