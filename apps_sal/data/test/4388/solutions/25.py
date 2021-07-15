n = input()
x = list()
for i in range(3):
    if n[i] == "1":
        x.append("9")
    else:
        x.append("1")
print(x[0] + x[1] + x[2])
