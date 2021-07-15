string = input()

hon = ["2", "4", "5", "7", "9"]
pon = ["0", "1", "6", "8"]

if string[-1] in hon:
    print("hon")
elif string[-1] in pon:
    print("pon")
else:
    print("bon")
