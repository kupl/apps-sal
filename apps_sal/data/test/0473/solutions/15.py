a = input()
q1, q2, q3, q4 = int(a[0]), int(a[1]), int(a[3]), int(a[4])
b = input()
w1, w2, w3, w4 = int(b[0]), int(b[1]), int(b[3]), int(b[4])
ww = (q3*10 + q4) + (q1*10 + q2)*60
qq = (w3*10 + w4) + (w1*10 + w2)*60
s = ""
if ww == qq:
    print("00:00")
elif (ww - qq) > 0:
    if(ww - qq) // 60 > 9:
        d = str((ww - qq)//60)
        s += d
    else:
        s += "0"
        d = str((ww - qq)//60)
        s += d
    s += ":"
    if (ww - qq) % 60 > 9:
        d = str((ww - qq)%60)
        s += d
    else:
        s += "0"
        d = str((ww - qq)%60)
        s += d 
    print(s)
else:
    if(ww - qq + 1440) // 60 > 9:
            d = str((ww - qq+ 1440)//60)
            s += d
    else:
        s += "0"
        d = str((ww - qq+ 1440)//60)
        s += d
    s += ":"
    if (ww - qq + 1440) % 60 > 9:
        d = str((ww - qq + 1440)%60)
        s += d
    else:
        s += "0"
        d = str((ww - qq + 1440)%60)
        s += d   
    print(s)


