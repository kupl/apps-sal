string = list(input())

left = []
right = []
leftTotal = 0
rightTotal = 0
rightSide = False
pivot = -1
for i in range(len(string)):
    if string[i] == "^":
        pivot = i

for i in range(len(string)):
    if "1" <= string[i] <= "9":
        if rightSide == False:
            leftTotal += (int(string[i]) * (pivot - i))
        else:
            rightTotal += (int(string[i]) * (i - pivot))

if leftTotal > rightTotal:
    print("left")
elif leftTotal < rightTotal:
    print("right")
else:
    print("balance")
