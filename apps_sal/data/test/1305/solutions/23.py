x = int(input())
stri = input().split()
bill = [int(p) for p in stri]
temp = 0


rem = [0, 0, 0]

for x in bill:
    if(bill[0] != 25):
        temp = 0
        break
    if(x == 25):
        rem[0] = rem[0] + 25
        temp = 1
    elif(x == 50):
        if(rem[0] != 0):
            rem[0] -= 25
            temp = 1
            rem[1] += 50
        else:
            temp = 0
            break

    else:
        if(rem[1] >= 50 and rem[0] >= 25):
            rem[0] -= 25
            rem[1] -= 50
            temp = 1
        elif(rem[0] >= 75):
            rem[0] -= 75
            temp = 1
        else:
            temp = 0
            break

        rem[2] = rem[2] + 100


if(temp == 0):
    print("NO")
else:
    print("YES")
