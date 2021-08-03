x = int(input()) % 10

if x == 3:
    print("bon")
elif x in {0, 1, 6, 8}:
    print("pon")
else:
    print("hon")
