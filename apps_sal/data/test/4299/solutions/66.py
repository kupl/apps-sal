n = input()
hon = "24579"
pon = "0168"
x = n[len(n) - 1]
if x in hon:
    print("hon")
elif x in pon:
    print("pon")
else:
    print("bon")
