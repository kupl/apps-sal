n = input()
if len(n) < 5:
    if int(n) % 4 == 0:
        print(4)
    else:
        print(0)
elif int(n[-2:]) % 4 == 0:
    print(4)
else:
    print(0)
