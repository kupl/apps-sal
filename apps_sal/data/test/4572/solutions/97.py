s = input()
c = "a"
while c <= "z":
    if s.find(c) == -1:
        print(c)
        break
    if c == "z":
        print("None")
    c = chr(ord(c) + 1)


