l = int(input())
a = input()
lena = len(a)
if lena % l != 0:
    ans = "1" + ("0" * (l - 1))
    ans = ans * (lena // l + 1)
    print(ans)
else:
    seg = lena // l
    now = a[0:l]
    flag = 0
    for i in range(seg):
        if now > a[i * l:(i + 1) * l]:
            flag = 1
            break
        elif now < a[i * l:(i + 1) * l]:
            break
    if flag == 0:
        if now.count("9") == l:
            now = "1" + "0" * (l - 1)
            seg += 1
        else:
            now = str(int(now) + 1)
    print(now * seg)
