n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = 0
while True:
    if len(a) == 0:
        break
    if a[0] <= k:
        cnt += 1
        a = a[1:]
        continue
    elif a[-1] <= k:
        cnt += 1
        a = a[:-1]
        continue
    else:
        break
print(cnt)
