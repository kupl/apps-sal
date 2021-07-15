z = 0
for i, c in enumerate(input().replace("g", "r")):
    if i % 2 == 0 and c == "r":
        pass
    elif i % 2 == 0 and c == "p":
        z -= 1
    elif c == "p":
        pass
    else:
        z += 1
print(z)

