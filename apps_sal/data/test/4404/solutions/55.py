a = input()

y = int(a[0:4])
m = int(a[5:7])

if y < 2019:
    print("Heisei")
elif y == 2019 and m <= 4:
    print("Heisei")
else:
    print("TBD")
