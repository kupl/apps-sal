S = input()
y = int(S[:4])
m = int(S[5:7])
d = int(S[8:])
if y < 2019:
    print("Heisei")
elif y == 2019 and m < 4:
    print("Heisei")
elif y == 2019 and m == 4 and d <= 30:
    print("Heisei")
else:
    print("TBD")
