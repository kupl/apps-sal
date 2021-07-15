day = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
a = input()
b = input()
i = day.index(a)
if day[i] == b or day[(i + 2) % 7] == b or day[(i + 3) % 7] == b:
    print("YES")
else:
    print("NO")

