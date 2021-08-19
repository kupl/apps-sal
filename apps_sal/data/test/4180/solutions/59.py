n = input()
if int(n[-3:]) == 0:
    print(0)
else:
    print(1000 - int(n[-3:]))
