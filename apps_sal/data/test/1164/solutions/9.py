s = input()
ans = 0
d = ""
for i in range(len(s)):
    if s[i] in "0123456789.":
        d += s[i]
    else:
        si = ""
        if len(d):
            for j in range(len(d)):
                if d[j] != ".":
                    si += d[j]
            si1 = int(si)
            if (len(d) >= 3 and d[-3] != ".") or len(d) < 3:
                si1 *= 100
            #print(si1)
            ans += si1
        d = ""
si = ""
for j in range(len(d)):
    if d[j] != ".":
        si += d[j]
    si1 = int(si)
if (len(d) >= 3 and d[-3] != ".") or len(d) < 3:
    si1 *= 100
ans += si1
if ans < 10:
    print("0.0{}".format(ans))
elif ans < 100:
    print("0.{}".format(ans))
else:
    ansl = str(ans)[::-1]
    ansi = ansl[0] + ansl[1] + "."
    for i in range(2, len(ansl)):
        if i % 3 == 2 and i != 2:
            ansi += "."
        ansi += ansl[i]
    if ans % 100 == 0:
        a = ansi[::-1]
        print(a[:-3])
    else:
        print(ansi[::-1])
