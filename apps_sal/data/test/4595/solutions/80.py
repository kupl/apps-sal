a = input()
for i in range(len(a)):
    if a[i] == "A":
        b = i
        break
for k in range(len(a)):
    if a[-k - 1] == "Z":
        c = k
        break
print(len(a) - c - b)
