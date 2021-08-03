X = input()

if int(X[-1]) in [3]:
    print("bon")
elif int(X[-1]) in [0, 1, 6, 8]:
    print("pon")
else:
    print("hon")
