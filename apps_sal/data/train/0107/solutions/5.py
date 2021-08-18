t = int(input())
while(t > 0):
    t = t - 1
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])
    d = int(l[3])
    if(a != 0):
        if((a + b) % 2 == 1):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
    else:
        if(d >= 1 and (a + b) % 2 == 1):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
    if(b != 0):
        if((a + b) % 2):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
    else:
        if(c >= 1 and (a + b) % 2 == 1):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
    if(c != 0):
        if((a + b) % 2 == 0):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
    else:
        if(b >= 1 and (a + b) % 2 == 0):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
    if(d != 0):
        if((a + b) % 2 == 0):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
    else:
        if(a >= 1 and (a + b) % 2 == 0):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
    print()
