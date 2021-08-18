k = int(input())
gx, gy = list(map(int, input().split()))
if k % 2 == 0 and (gx + gy) % 2:
    print((-1))
    return
flgx = 1
flgy = 1
if gx < 0:
    flgx -= 2
    gx *= -1
if gy < 0:
    flgy -= 2
    gy *= -1
px = 0
py = 0
ansls = []
while True:
    if (gx - px + gy - py) <= 2 * k:
        break
    if gx - px >= k:
        px += k
    elif gy - py >= k:
        py += k
    ansls.append((px, py))
if gx - px + gy - py <= 2 * k:
    if gx - px + gy - py == 2 * k:
        if px + k <= gx:
            px += k
        else:
            py += k
        ansls.append((px, py))
    if gx - px + gy - py == k:
        ansls.append((gx, gy))
    else:
        if (gx - px + gy - py) % 2:
            if px + k <= gx:
                px += k
            elif py + k <= gy:
                py += k
            elif px + py + k <= gx + gy:
                py += k - (gx - px)
                px = gx
            else:
                py -= gx - px
                px -= k - (gx - px)
            ansls.append((px, py))
        if gx - px <= gy - py:
            ansls.append((px + (gx - px + gy - py) // 2 - k, py + (gx - px + gy - py) // 2))
        else:
            ansls.append((px + (gx - px + gy - py) // 2, py + (gx - px + gy - py) // 2 - k))
        ansls.append((gx, gy))
for i in range(len(ansls) - 1):
    if abs(ansls[i + 1][0] - ansls[i][0]) + abs(ansls[i + 1][1] - ansls[i][1]) != k:
        print("error")
print((len(ansls)))
for x, y in ansls:
    print((x * flgx, y * flgy))
