n, h = map(int, input().split())
mxa = 0
dmg = 0
cnt = 0
di = []
for i in range(n):
    a, b = map(int, input().split())
    di.append(b)
    if a > mxa:
        mxa = a
di.sort(reverse=True)
for j in di:
    if j >= mxa:
        dmg += j
        cnt += 1
        if dmg >= h:
            break
if dmg < h:
    cnt += (h - dmg) // mxa
    if (h - dmg) % mxa != 0:
        cnt += 1
print(cnt)
