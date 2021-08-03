c = [['1', '3', '5', '7', '8', '10', '12'], ['4', '6', '9', '11'], ['2']]

a, b = input().split(' ')

if a in c[0] and b in c[0]:
    print("Yes")
elif a in c[1] and b in c[1]:
    print("Yes")
elif a in c[2] and b in c[2]:
    print("Yes")
else:
    print("No")
