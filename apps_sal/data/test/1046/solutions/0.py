
n = int(input())
arr = list(map(int, input().split()))


cnt = 0
clast, llast = -1, -1

arr = sorted(arr)

bad = False
for i in arr:
    if i > 0:
        if i == clast:
            cnt += 1
            if clast == llast:
                bad = True
        llast = clast
        clast = i
if bad == False:
    print(cnt)
else:
    print(-1)
