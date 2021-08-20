a = input()
for i in range(len(a)):
    if a[i] == 'A':
        b = i
        break
for j in range(len(a) - 1, -1, -1):
    if a[j] == 'Z':
        c = j
        break
print(c - b + 1)
