a = input()
b = input()
j = 0
s = 1
for i in range(len(b)):
    if b[i] == a[j]:
        s = s + 1
        j = j + 1
print(s)
