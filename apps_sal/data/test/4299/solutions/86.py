word = list(input())
n = int(len(word)) - 1
s = word[n]
if s == "0" or s == "1" or s == "6" or s == "8":
    print("pon")
elif s == "3":
    print("bon")
else:
    print("hon")
