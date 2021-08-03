a, w, t, r = 0, 0, 0, 0
for _ in range(int(input())):
    s = input()
    if(s == "AC"):
        a += 1
    elif(s == "WA"):
        w += 1
    elif(s == "TLE"):
        t += 1
    else:
        r += 1
print("AC x", a)
print("WA x", w)
print("TLE x", t)
print("RE x", r)
