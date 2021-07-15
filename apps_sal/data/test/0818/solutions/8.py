NumLength = int(input())
tens = 100

if NumLength <= 2:
    print("-1")
elif NumLength == 3:
    print("210")
else:
    tens = tens * pow(10, (NumLength - 3))
    tens = tens + 210 - (tens % 210)
    print(tens)
