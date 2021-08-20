m = int(input())
dou = 0
fir = []
sec = []
non = []
(d, f, s, n) = (0, 0, 0, 0)
for i in [0] * m:
    (a, b) = list(map(int, input().split()))
    if a == 11:
        dou += b
        d += 1
    elif a == 1:
        sec.append(b)
        s += 1
    elif a == 10:
        fir.append(b)
        f += 1
    else:
        non.append(b)
        n += 1
fir.sort(reverse=True)
sec.sort(reverse=True)
if not d + f * s:
    print(0)
    quit()
else:
    m = min(f, s)
    ans = dou + sum(fir[:m]) + sum(sec[:m])
    non = non + fir[m:] + sec[m:]
    non.sort(reverse=True)
    print(ans + sum(non[:d]))
