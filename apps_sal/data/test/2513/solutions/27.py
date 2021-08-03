n = int(input())
s = input()
a = "SS"
ct = 1
while ct < 7:
    for i in range(n - 1):
        p = a[i]
        q = "A"
        if a[i] == "S":
            q = "W"
        else:
            q = "S"
        if a[i + 1] == "S":
            if s[i + 1] == "o":
                a = a + a[i]
            else:
                a = a + q
        else:
            if s[i + 1] == "o":
                a = a + q
            else:
                a = a + a[i]
    if a[0] == a[n]:
        if a[0] == "S" and s[0] == "o" and a[n - 1] == a[1]:
            print(a[0:n])
            break
        elif a[0] == "S" and s[0] != "o" and a[n - 1] != a[1]:
            print(a[0:n])
            break
        elif a[0] == "W" and s[0] == "o" and a[n - 1] != a[1]:
            print(a[0:n])
            break
        elif a[0] == "W" and s[0] != "o" and a[n - 1] == a[1]:
            print(a[0:n])
            break
        else:
            ct = ct + 1
        if ct == 2:
            a = "SW"
        elif ct == 3:
            a = "WS"
        elif ct == 4:
            a = "WW"
        else:
            print(-1)
            break
    else:
        ct = ct + 1
        if ct == 2:
            a = "SW"
        elif ct == 3:
            a = "WS"
        elif ct == 4:
            a = "WW"
        else:
            print(-1)
            break
