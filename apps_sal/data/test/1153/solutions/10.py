n, m = list(map(int, input().split()))
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

sm1 = sm2 = 0
i = j = 0
cnt = 0

moveX = moveY = True

while i < len(xs):
    if moveX:
        sm1 += xs[i]
    if moveY:
        sm2 += ys[j]
    if sm1 < sm2:
        i += 1
        moveX = True
        moveY = False
    elif sm1 > sm2:
        j += 1
        moveX = False
        moveY = True
    else:
        sm1 = sm2 = 0
        cnt += 1
        i += 1
        j += 1
        moveX = True
        moveY = True

print(cnt)

