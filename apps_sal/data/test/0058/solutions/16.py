n = int(input())
a = int(input())
b = int(input())
cnt = 0
l = 0
al = 4
bl = 2
cnt += 1
l = n
while al or bl:
    if al > bl:
        if l - a >= 0 and al:
            al -= 1
            l -= a
            continue
        elif l - b >= 0 and bl:
            bl -= 1
            l -= b
            continue
        else:
            l = n
            cnt += 1
            continue
    elif l - b >= 0 and bl:
        bl -= 1
        l -= b
        continue
    elif l - a >= 0 and al:
        al -= 1
        l -= a
        continue
    else:
        l = n
        cnt += 1
        continue
print(cnt)
