a = input()
for i in range(len(a)):
    if a[i] == "A":
        b = i
        break
for j in range(len(a)):
    if a[j] == "Z":
        c = j
print((c - b + 1))
