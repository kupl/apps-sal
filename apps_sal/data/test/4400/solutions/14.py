s = input()
j = 0
ren = 0
for num in range(3):
    if s[num] == "R":
            if ren == 1:
                j += 1
            else:
                j = 1
            ren = 1
    else:
        ren = 0
print(j)

