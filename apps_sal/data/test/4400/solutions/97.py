s = input()

a = s[0]
b = s[1]
c = s[2]

if a == "S" and b == "S" and c == "S":
    print("0")

elif ((a != "S" and b == "S" and c == "S")
    or (a == "S" and b == "S" and c != "S")
    or (a == "S" and b != "S" and c == "S")
        or (a != "S" and b == "S" and c != "S")):

    print("1")

elif ((a != "S" and b != "S" and c == "S")
      or (a == "S" and b != "S" and c != "S")):

    print("2")

else:
    print("3")
