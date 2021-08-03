t = int(input())
for you in range(t):
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])
    d = int(l[3])
    z = a + b
    if(z % 2 == 0):
        print("Tidak Tidak", end=" ")
        if(b > 0 or c > 0):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
        if(a > 0 or d > 0):
            print("Ya")
        else:
            print("Tidak")
    else:
        if(a > 0 or d > 0):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
        if(b > 0 or c > 0):
            print("Ya", end=" ")
        else:
            print("Tidak", end=" ")
        print("Tidak Tidak")
