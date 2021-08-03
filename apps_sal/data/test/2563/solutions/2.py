for t in range(int(input())):
    s = input()
    l = len(s)
    eve = ""
    odd = ""
    for i in range(l):
        if((ord(s[i]) - ord("0")) % 2 == 0):
            eve += s[i]
        else:
            odd += s[i]
    e0 = len(eve)
    o0 = len(odd)
    e = 0
    o = 0
    a = ""
    for i in range(l):
        if(o == o0):
            a += eve[e]
            e += 1
        elif(e == e0):
            a += odd[o]
            o += 1
        elif(ord(eve[e]) > ord(odd[o])):
            a += odd[o]
            o += 1
        else:
            a += eve[e]
            e += 1
    print(a)
