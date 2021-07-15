x = int(input())
add = int(x/2)
for i in range(x):
    for j in range(x):
        a1 = i-add
        b2 = j-add
        if abs(a1) + abs(b2) <= add:
            print ("D", end="")
        else:
            print("*", end = "")
    print ()

