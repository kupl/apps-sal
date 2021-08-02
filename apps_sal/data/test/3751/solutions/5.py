program = input()

to_use = "abcdefghijklmnopqrstuvwxyz"
used = ""
legal = True

for char in program:
    if char in used:
        continue
    else:
        if char == to_use[0]:
            used += to_use[0]
            to_use = to_use[1:]
        else:
            legal = False
            break

if legal:
    print("YES")
else:
    print("NO")
