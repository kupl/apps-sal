t = int(input())
for _ in range(t):
    r, g, b, w = map(int, input().split())
    if(r % 2 == 0 and g % 2 == 0 and b % 2 == 0 and w % 2 == 0):
        print("Yes")
    elif(r % 2 == 0 and g % 2 == 0 and b % 2 == 0):
        print("Yes")
    elif(r % 2 == 0 and g % 2 == 0 and w % 2 == 0):
        print("Yes")
    elif(r % 2 == 0 and b % 2 == 0 and w % 2 == 0):
        print("Yes")
    elif(w % 2 == 0 and g % 2 == 0 and b % 2 == 0):
        print("Yes")
    else:
        if(r > 0 and g > 0 and b > 0):
            r -= 1
            g -= 1
            b -= 1
            w += 3
            if(r % 2 == 0 and g % 2 == 0 and b % 2 == 0 and w % 2 == 0):
                print("Yes")
            elif(r % 2 == 0 and g % 2 == 0 and b % 2 == 0):
                print("Yes")
            elif(r % 2 == 0 and g % 2 == 0 and w % 2 == 0):
                print("Yes")
            elif(r % 2 == 0 and b % 2 == 0 and w % 2 == 0):
                print("Yes")
            elif(w % 2 == 0 and g % 2 == 0 and b % 2 == 0):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
