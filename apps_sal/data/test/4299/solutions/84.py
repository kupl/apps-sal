N = input()
if N[len(N) - 1] == "3":
    print("bon")
elif (N[len(N) - 1] == "0") or (N[len(N) - 1] == "1") or (N[len(N) - 1] == "6") or (N[len(N) - 1] == "8"):
    print("pon")
else:
    print("hon")
