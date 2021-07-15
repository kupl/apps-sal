
tt = int(input())

for loop in range(tt):

    z = 0
    o = 0

    s = input()
    for i in s:
        if i == "0":
            z += 1
        else:
            o += 1

    if min(z,o) % 2 == 0:
        print ("NET")
    else:
        print ("DA")

