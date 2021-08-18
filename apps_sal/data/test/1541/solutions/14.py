n = input()

zn = 0
wyn = 0
for i in range(len(n)):
    if n[i] == '^':
        zn = i
for i in range(len(n)):
    if n[i] != '^' and n[i] != '=':
        wyn += (zn - i) * int(n[i])

if wyn == 0:
    print("balance")
elif wyn > 0:
    print("left")
else:
    print("right")
