k = 0
ad = []
res = 0
for _ in range(int(input())):
    s = input()
    if res > 2**32 - 1:
        break
    if len(ad) > 0:
        if (res + ad[-1][0] * ad[-1][1]) > 2**32 - 1:
            res = res + (ad[-1][0] * ad[-1][1])
            break

    if s[:3] == 'add':
        if len(ad) > 0:
            ad[-1][0] += 1
        else:
            res += 1
    elif s[:3] == 'end':
        k = ad[-1][0] * ad[-1][1]
        ad.pop()
        if len(ad) > 0:
            ad[-1][0] += k
        else:
            res += k
        k = 0
    else:
        p = int(s[4:])
        ad.append([0, p])
if res > 2**32 - 1:
    print('OVERFLOW!!!')
else:
    print(res)
