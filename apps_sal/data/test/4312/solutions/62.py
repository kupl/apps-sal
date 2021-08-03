monsters = input()
list = monsters.split(" ")
a = int(list[0])
b = int(list[1])
c = int(list[2])
d = int(list[3])
while True:
    c = c - b
    if c <= 0:
        print("Yes")
        break
    a = a - d
    if a <= 0:
        print("No")
        break
