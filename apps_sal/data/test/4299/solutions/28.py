N = input()

PON = ["0", "1", "6", "8"]

BON = ["3"]

if N[-1:] in BON:
    print("bon")
elif N[-1:] in PON:
    print("pon")
else:
    print("hon")
