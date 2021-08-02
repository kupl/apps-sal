x = input()
if int(x[0]) > int(x[1]):
    print(x[0] * 3)
elif int(x[0]) == int(x[1]):
    if int(x[0]) >= int(x[2]):
        print(x[0] * 3)
    else:
        print(str(int(x[0]) + 1) * 3)
else:
    print(str(int(x[0]) + 1) * 3)
