a = input()
b = input()
i = 0
while b:
    if b[0] == a[i]:
        i += 1
    b = b[1:]
print(i + 1)
