n = int(input())

line = input()

Anton = 0
Danik = 0

for x in line:
    if x == "A":
        Anton = Anton + 1
    else:
        Danik = Danik + 1

if Anton == Danik:
    print("Friendship")
elif Anton > Danik:
    print("Anton")
else:
    print("Danik")
