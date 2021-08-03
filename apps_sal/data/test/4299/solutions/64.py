num = input()
numline = list(num)
a = int(numline[len(numline) - 1])
if(a == 3):
    print("bon")
elif(a == 0 or a == 1 or a == 6 or a == 8):
    print("pon")
else:
    print("hon")
